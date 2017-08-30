# Item Catalog Application
### _by Arvind Rathee_
Item Catalog Application project, part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
## About
A web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items. This project uses Python 3.4 .
## Python Libraries
This project uses following Libraries:
- Random, String, Http2lib, Json (Comes along with python)
- SQLAlchemy 
    ```python
    pip install sqlalchemy
    ```
- Flask
    ```python
    pip install flask
    ```
- OAuth2
    ```python
    pip install oauth2
    ```
- Requests
    ```python
    pip install requests
    ```
## Project Content
- app.py - This is the main file and contain main program.
- database_setup.py - This file contain the structure of the database to be implemented.
- db_items.py - This file contain the code to populate the database with dummy data.
- client_secrets.json - This file contain info about the google api.
- catalog.db - Database created after running database_setup.py and db_items.py
- templates/ - This folder contain all the templates used to render the website.
- static/ - This folder contain static files like CSS and JS files
## Working
* Download the project zip file to you computer and unzip the file or clone this repository to your desktop.
* Navigate to the project directory.
* Open terminal and run following command
    ```python
    python app.py
    ```
* Now the application is running locally.
* Visit [here](http://localhost:5000/) to view the application.
* If you want to run the application with your own credentials than follow these steps :
    ### _Get an API key_
    1. Login to your google account.
    2. Go to the [Google API Console](https://console.developers.google.com/flows/enableapi?apiid=places_backend&reusekey=true).
    3. Create or select a project.
    4. Click Continue to enable the API.
    5. On the Credentials page, get an API key (and set the API key restrictions).
        -> For More Info About the API Click [Here](https://developers.google.com/identity/protocols/OAuth2).
    6. Download your client_secrets.json file.
    ### Running the Application
    - Replace client_secrests.json file with your file.
    - Replace data-clientid parameter value in login.html with your own client ID.
    - Now open Terminal and run following commands
        ```python
        # Setting the database
        python database_setup.py
        # Populate the database with dummy data
        python db_items.py
        # Now run main file
        python app.py
        ```

## JSON Endpoints
The following are open to the public:
* Level JSON: /level/JSON - Displays all levels

* Level Courses JSON: /level/<level_name>/JSON/ - Displays courses for a specific level

* Course JSON: /level/<level_name>/<course_name>/JSON/ - Displays a specific course.
