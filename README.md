# Linux Server Configuration
### _by Arvind Rathee_
Linux server configuration project, part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
## Description
I took a baseline installation of a Linux distribution (Ubuntu) on a virtual machine and prepare it to host Item Catalog web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.
The application meant to be deployed is the **_Item catalog app_**, previously developed for [Project 4](https://github.com/BulletLock/Item-Catalog).
I have used **_Google Cloud Platform_** to host my application.

## Useful info

IP address: 130.211.160.57 .

Accessible SSH port: 2200 .

Application URL: [http://130.211.160.57.nip.io](http://130.211.160.57.nip.io) .

# Step by step walkthrough

## 1 - Starting an Instance
### Sign Up 
1. Visit [here](https://accounts.google.com/signin/v2/identifier?service=cloudconsole&passive=1209600&osid=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Ffreetrial%3F_ga%3D2.258335050.-1966546917.1504092754%26ref%3Dhttps%3A%2F%2Fcloud.google.com%2F&followup=https%3A%2F%2Fconsole.cloud.google.com%2Ffreetrial%3F_ga%3D2.258335050.-1966546917.1504092754%26ref%3Dhttps%3A%2F%2Fcloud.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin) and login with your gogole account or sign up for a new account .
2. Proceed with the registration process, you will be asked for billing details and will be charged a small amount but that amount will be credited back to you.
3. Now you have a free account on _Google Cloud Platform_ .
### Create an instance
1. Now from menu go to compute engine > VM instances.
2.  Click the Create instance button.
3. In the Boot disk section, click Change to begin configuring your boot disk.
4. In the OS images tab, choose the Ubuntu 16.04 image.
5. Click Select.
6. In the Firewall section, select Allow HTTP traffic.
7. Click the Create button to create the instance. 
8. A VM instance has been created.
### Connect to your instance
1. In the Cloud Platform Console, go to the VM Instances page. 
2. In the list of virtual machine instances, click SSH in the row of the instance that you want to connect to. 
    * The SSH connection can be made via a browser window or using gcloud or using a window application like PUTTY.
***Note*** - I will suggest using browser SSH window for tasks below because by default SSH port is 22 and many ISP block it, but later i will change the port and will tell you how to use SSH using PUTTY. 

# 2 - Update all currently installed packages

1. `$ sudo apt-get update`.
2. `$ sudo apt-get upgrade`.
3. Install *finger*, a utility software to check users' status: `$ apt-get install finger`.

# 3 - Configure the local timezone to UTC

1. Open time configuration dialog and set it to UTC with: `$ sudo dpkg-reconfigure tzdata`.
2. Install *ntp daemon ntpd* for a better synchronization of the server's time over the network connection: `$ sudo apt-get install ntp`.

Source: [UbuntuTime](https://help.ubuntu.com/community/UbuntuTime).

# 4 - Change the SSH port from 22 to 2200
1. Using the menubar go to VPC Network > Firewall Rules.
2. Set up a custom firewall rule to enable access to port 2200 .
3. Now open sshd_config using following command : `$ sudo nano /etc/ssh/sshd_config`. Find the *Port* line and edit it to *2200*.
4. `$ sudo service ssh restart`.
5. Port has been changed to 2200.

***Note*** - Do not close the SSH window because you will lock out yourself if you close the window now. You must open atleast two windows for safety. You must configure UFW after this step.

# 5 - Configure the Uncomplicated Firewall (UFW)

Project requirements need the server to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).

1. `$ sudo ufw allow 2200/tcp`.
2. `$ sudo ufw allow 80/tcp`.
3. `$ sudo ufw allow 123/udp`.
4. `$ sudo ufw enable`.
5. `$ sudo service ssh restart`.

# 6 - Create a new user named *grader*
1. Create a new user called *grader* : `$ sudo adduser grader` .
2. Give new user sudo privilages : `$ sudo usermod -aG sudo grader` .

# 7  - Configure the key-based authentication for *grader* user
### Using Terminal
1. Generate an encryption key **on your local machine** with: `$ ssh-keygen -f ~/.ssh/udacity_key.rsa`.
2. Log into the remote VM as *root* user through ssh and create the following file: `$ touch /home/grader/.ssh/authorized_keys`.
3. Copy the content of the *udacity_key.pub* file from your local machine to the */home/grader/.ssh/authorized_keys* file you just created on the remote VM. Then change some permissions:
	1. `$ sudo chmod 700 /home/grader/.ssh`.
	2. `$ sudo chmod 644 /home/grader/.ssh/authorized_keys`.
	3. Finally change the owner from *root* to *grader*: `$ sudo chown -R grader:grader /home/grader/.ssh`.

### Using PUTTYgen
1. Open the PuTTYgen program.
2. For Type of key to generate, select SSH-2 RSA.
3. Click the Generate button.
4. Move your mouse in the area below the progress bar. When the progress bar is full, PuTTYgen generates your key pair.
5. In your comment field add 'grader'.
6. Type a passphrase in the Key passphrase field. Type the same passphrase in the Confirm passphrase field. You can use a key without a passphrase, but this is not recommended.
7. Click the Save private key button to save the private key. Warning! You must save the private key. You will need it to connect to your machine.
8. Right-click in the text field labeled Public key for pasting into OpenSSH authorized_keys file and choose Select All.
9. Right-click again in the same text field and choose Copy.
10. Now using menubar on google go to VM instances > Metadata.
11. On the Metadata page go to SSH keys tab.
12. Click on Edit.
13. CLick on Add Item and paste the key you copied from the grey box.
14. Save it.

# 8 - Enforce key-based authentication
1. `$ sudo nano /etc/ssh/sshd_config`. Find the *PasswordAuthentication* line and edit it to *no*.
2. `$ sudo service ssh restart`.

# 9 - Install Apache, mod_wsgi

1. `$ sudo apt-get install apache2`.
2. Mod_wsgi is an Apache HTTP server mod that enables Apache to serve Flask applications. Install *mod_wsgi* with the following command: `$ sudo apt-get install libapache2-mod-wsgi python-dev`.
3. Enable *mod_wsgi*: `$ sudo a2enmod wsgi`.
3. `$ sudo service apache2 start`.

# 10 - Install Git

1. `$ sudo apt-get install git`.

# 11 - Clone the Catalog app from Github

1. `$ cd /var/www/html`. Then: `$ sudo mkdir catalog`.
2. Change owner for the *catalog* folder: `$ sudo chown -R grader:grader catalog`.
3. Move inside that newly created folder: `$ cd /catalog` and clone the catalog repository from Github: `$ git clone https://github.com/BulletLock/Item-Catalog.git catalog`.
4. Make a *catalog.wsgi* file to serve the application over the *mod_wsgi*. That file should look like this:

    ```python
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, "/var/www/html/catalog/")
    
    from catalog import app as application
    ```
5. Some tweaks were needed to deploay the catalog app, so I made a *deployment* branch which slightly differs from the *master*. You can check the new code by changing the branch of this repo from master to deployment.

**Notes**: the *.git* folder will be inaccessible from the web without any particular setting. The only directory that can be listed in the browser will be the static folder: [static assets](http://130.211.160.57.nip.io/static/).

# 12 - Install virtual environment, Flask and the project's dependencies

1. Install *pip*, the tool for installing Python packages: `$ sudo apt-get install python-pip`.
2. If *virtualenv* is not installed, use *pip* to install it using the following command: `$ sudo pip install virtualenv`.
3. Move to the *catalog* folder: `$ cd /var/www/html/catalog`. Then create a new virtual environment with the following command: `$ sudo virtualenv venv`.
4. Activate the virtual environment: `$ source venv/bin/activate`.
5. Change permissions to the virtual environment folder: `$ sudo chmod -R 777 venv`.
6. Install Flask: `$ sudo pip install Flask`.
7. Install all the other project's dependencies: `$ sudo pip install -r requirment.txt`. 
8. Along with this also run coomand : `$ sudo apt-get install python-flask` .

# 13 - Configure and enable a new virtual host

1. Create a virtual host conifg file: `$ sudo nano /etc/apache2/sites-available/catalog.conf`.
2. Paste in the following lines of code:
    ```
    <VirtualHost *:80>
        ServerName 130.211.160.57
        ServerAlias ec2-52-34-208-247.us-west-2.compute.amazonaws.com
        ServerAdmin admin@52.34.208.247
        WSGIDaemonProcess catalog python-path=/var/www/html/catalog:/var/www/html/catalog/venv/lib/python2.7/site-packages
        WSGIProcessGroup catalog
        WSGIScriptAlias / /var/www/html/catalog/catalog.wsgi
        <Directory /var/www/html/catalog/catalog/>
            Order allow,deny
            Allow from all
        </Directory>
        Alias /static /var/www/html/catalog/catalog/static
        <Directory /var/www/html/catalog/catalog/static/>
            Order allow,deny
            Allow from all
        </Directory>
        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
    ```
* The **WSGIDaemonProcess** line specifies what Python to use and can save you from a big headache. In this case we are explicitly saying to use the virtual environment and its packages to run the application.

3. Enable the new virtual host: `$ sudo a2ensite catalog`.

# 14 - Install and configure PostgreSQL

1. Install some necessary Python packages for working with PostgreSQL: `$ sudo apt-get install libpq-dev python-dev`.
2. Install PostgreSQL: `$ sudo apt-get install postgresql postgresql-contrib`.
3. Postgres is automatically creating a new user during its installation, whose name is 'postgres'. That is a tusted user who can access the database software. So let's change the user with: `$ sudo su - postgres`, then connect to the database system with `$ psql`.
4. Create a new user called 'catalog' with his password: `# CREATE USER catalog WITH PASSWORD 'catalog';`.
5. Give *catalog* user the CREATEDB capability: `# ALTER USER catalog CREATEDB;`.
6. Create the 'catalog' database owned by *catalog* user: `# CREATE DATABASE catalog WITH OWNER catalog;`.
7. Connect to the database: `# \c catalog`.
8. Revoke all rights: `# REVOKE ALL ON SCHEMA public FROM public;`.
9. Lock down the permissions to only let *catalog* role create tables: `# GRANT ALL ON SCHEMA public TO catalog;`.
10. Log out from PostgreSQL: `# \q`. Then return to the *grader* user: `$ exit`.
11. Inside the Flask application, the database connection is now performed with: 
    ```python
    engine = create_engine('postgresql://catalog:catalog@catalog/catalog')
    ```
12. Setup the database with: `$ python /var/www/html/catalog/catalog/database_setup.py`.
13. Populate database with: `$ python /var/www/html/catalog/catalog/db_items.py`. 
14. Create a user named catalog using following command : `$ sudo adduser catalog`
15. set password for this user to 'catalog'.
16. now you can access catalog database directly using command : `$ sudo -i -u catalog psql`
17. To prevent potential attacks from the outer world we double check that no remote connections to the database are allowed. Open the following file: `$ sudo nano /etc/postgresql/9.5/main/pg_hba.conf` and edit it, if necessary, to make it look like this: 
    ```
    local   all             postgres                                peer
    local   all             all                                     peer
    host    all             all             127.0.0.1/32            md5
    host    all             all             ::1/128                 md5
    ```
Source: [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps).

# 15 - Update OAuth authorized JavaScript origins

1. To let users correctly log-in change the authorized URI to [http://130.211.160.57.nip.io](http://130.211.160.57.nip.io) on Google developer dashboards.

# 16 - Restart Apache to launch the app
1. `$ sudo service apache2 restart`.

# 17 - Access SSH using Putty
1. open putty.
2. Enter ` grader@130.211.160.57 ` in Host Name  and ` 2200 ` in Port.
3. In category go to SSH > Auth
4. Select private key file
5. click open and enter password if you are prompted.
