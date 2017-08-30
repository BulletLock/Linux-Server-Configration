from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc, DateTime, func
from sqlalchemy.orm import sessionmaker
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from .database_setup import Base, Level, Course, User
from functools import wraps
import random
import string
import httplib2
import json
import requests


app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Connect to Database and create database session
engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
# A DBSession() instance establishes all conversations with the database
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Update client_secrets.json with your Google API project information.
# Do not change this assignment.
CLIENT_ID = json.loads(
    open('/var/www/html/catalog/catalog/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

# Login decorator for checking if user is logged in or not
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

# Create anti-forgery state token
# Store it in the session for later validation.
@app.route('/login')
def showLogin():
    """This function creates an anti-forgery
        state token and renders login page """
    state = ''.join(random.choice(
                   string.ascii_uppercase + string.digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Exchange the one-time authorization code for a token and
        store the token in the session."""
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code, now compatible with Python3
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('/var/www/html/catalog/catalog/client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    print(access_token)
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h3>Welcome, '
    output += login_session['username']
    output += '!</h3>'
    flash("Welcome ! You are now logged in as %s" % login_session['username'])
    return output

# User Helper Functions


def createUser(login_session):
    """Creates User if they dosent exist in the database"""
    newUser = User(name=login_session['username'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    """Extracts User info from database"""
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    """Extracts email of user if user is present in the database"""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    """Revoke current user's token and reset their session."""
    access_token = login_session.get('access_token')
    print(access_token)
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print(result)
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        return redirect(url_for('showLevels'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# show all levels
@app.route('/')
def showLevels():
    """renders main page which displays latest content added to the database"""
    levels = session.query(Level).all()
    courses = session.query(Course).order_by(Course.created_date).limit(9).all()
    # Checks if user in session and renders page accordingly.
    if 'username' not in login_session:
        return render_template('public_levels.html',
                               levels=levels, courses=courses)
    else:
        return render_template('member_levels.html',
                               levels=levels, courses=courses)


# Show existing course in a level
@app.route('/<path:level_name>/')
def showLevel(level_name):
    """This renders courses present in particular category"""
    levels = session.query(Level).all()
    level = session.query(Level).filter_by(name=level_name).one()
    courses = session.query(Course).filter_by(level_id=level.id).all()
    if 'username' not in login_session:
        return render_template('public_level.html',
                               levels=levels, courses=courses, level=level)
    else:
        return render_template('member_level.html',
                               levels=levels, courses=courses, level=level)


# Show course info
@app.route('/<path:level_name>/<path:course_name>/')
def showCourse(level_name, course_name):
    """Renders course information"""
    level = session.query(Level).filter_by(name=level_name).one()
    course = session.query(Course).filter_by(name=course_name).one()
    if 'username' not in login_session:
        return render_template('public_course.html',
                               course=course, level=level)
    else:
        return render_template('member_course.html',
                               course=course, level=level)


# Create a new course
@app.route('/course/new/', methods=['GET', 'POST'])
@login_required
def newCourse():
    """Creates a new course"""
    if request.method == 'POST':
        level = session.query(Level).filter_by(
            name=request.form['level']).one()
        newCourse = Course(name=request.form['name'],
                           provider=request.form['provider'],
                           review=request.form['review'],
                           link=request.form['link'],
                           description=request.form['description'],
                           user_id=login_session['user_id'],
                           level_id=level.id)
        session.add(newCourse)
        session.commit()
        flash('New Course %s Successfully Created' % newCourse.name)
        return redirect(url_for('showLevel', level_name=level.name))
    else:
        return render_template('new_course.html')


# Edit existing course
@app.route('/<path:level_name>/<path:course_name>/edit/', methods=['GET', 'POST'])
@login_required
def editCourse(level_name, course_name):
    """Edit an existing course"""
    level = session.query(Level).filter_by(name=level_name).one()
    course = session.query(Course).filter_by(name=course_name).one()
    # If user is in session but is not creator of course than
    # this checks that and prompts user with not authorized message
    if course.user_id != login_session['user_id']:
        return """<script>function myFunction() {
                        alert('You are not authorized to edit this course.');
                        window.location = window.location.href.replace(
                        'edit/', '');}</script><body onload='myFunction()''>"""
    if request.method == 'POST':
        if request.form['name']:
            course.name = request.form['name']
        if request.form['description']:
            course.description = request.form['description']
        if request.form['provider']:
            course.provider = request.form['provider']
        if request.form['review']:
            course.review = request.form['review']
        if request.form['link']:
            course.link = request.form['link']
        if request.form['level']:
            new_level = session.query(Level).filter_by(
                name=request.form['level']).one()
            course.level_id = new_level.id
        session.add(course)
        session.commit()
        flash('Course Successfully Edited')
        return redirect(url_for('showLevel', level_name=level_name))
    else:
        return render_template('edit_course.html', course=course, level=level)


# Delete existing course
@app.route('/<path:level_name>/<path:course_name>/delete/', methods=['GET', 'POST'])
@login_required
def deleteCourse(level_name, course_name):
    """Delete an existing course"""
    level = session.query(Level).filter_by(name=level_name).one()
    course = session.query(Course).filter_by(name=course_name).one()
    # If user is in session but is not creator of course than
    # this checks that and prompts user with not authorized message
    if course.user_id != login_session['user_id']:
        return """<script>function myFunction() {
                        alert('You are not authorized to delete this course.');
                        window.location = window.location.href.replace(
                        'delete/', '');}</script>
                        <body onload='myFunction()''>"""
    if request.method == 'POST':
        session.delete(course)
        session.commit()
        flash('Course Successfully Deleted')
        return redirect(url_for('showLevels'))
    else:
        return render_template('delete_course.html',
                               level=level, course=course)


# JSON APIs to view Course Catalog Information
@app.route('/level/JSON/')
def levelsJSON():
    """This outputs entire level table as json data"""
    levels = session.query(Level).all()
    return jsonify(levels=[level.serialize for level in levels])


@app.route('/level/<level_name>/JSON/')
def levelJSON(level_name):
    """This outputs all the courses present
         in a particular level as json data"""
    print(level_name)
    level = session.query(Level).filter_by(name=level_name).one()
    courses = session.query(Course).filter_by(level_id=level.id).all()
    return jsonify(course=[i.serialize for i in courses])


@app.route('/level/<level_name>/<course_name>/JSON/')
def courseJSON(level_name, course_name):
    """This outputs particular course as json data"""
    level = session.query(Level).filter_by(name=level_name).one()
    courses = session.query(Course).filter_by(name=course_name).all()
    return jsonify(course=[i.serialize for i in courses])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
