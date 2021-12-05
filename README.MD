****Required Packages**
django
djangorestframework
psycopg2
requests
pandas
numpy

**To Install the packages use command**
    $ pip install package_name

**Steps For creating Project**
_**1)Creating a project using the command**_
	$ django-admin startproject project_name
From the command line, cd into a directory where we like to store our code, then run the following command
	$cd project_name
2)To verify our Django project works. Change into the outer project_name directory, if you haven’t already, and run the following commands
	$ py manage.py runserver

2a)Changing the port

By default, the runserver command starts the development server on the internal IP at port 8000.

If we want to change the servers port, pass it as a command-line argument. For example, this command starts the server on port 8080
	$ py manage.py runserver 8080

3)Creating the app
To create our app, make sure we are in the same directory as manage.py and type this command
	$ python manage.py startapp appname

4)Now we have to take care of settings.py
	4a)INSTALLED_APPS
		A list of strings designating all applications that are enabled in this Django installation. Each string should be a dotted Python path to:
		1)an application configuration class (preferred), or 
		2)a package containing an application.
	INSTALLED_APPS = [
    		'django.contrib.admin',
    		'django.contrib.auth',
    		'django.contrib.contenttypes',
    		'django.contrib.sessions',
    		'django.contrib.messages',
    		'django.contrib.staticfiles',
    		'myapp',
    		'rest_framework',
	]

	4b)DATABASES
		I am using database as Postgresql so we need to configure
	DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        	'NAME': 'DATABASE_NAME',
        	'USER': 'DATABASE_USERNAME',
        	'PASSWORD': 'DATABASE_PASSWORD',
        	'HOST': 'LOCALHOST/URL',
        	'PORT': 'PORT NUMBER',
    		}
	}
5)Create urls.py in app folder
	Here we have to store all our url patterns of our project.For every view (web page), we have to define separate url-pattern. End user can use url-patterns to access our webpages.
6)models.py
	 It contains the essential fields and behaviors of the data we are storing. Generally, each model maps to a single database table.
	 Each attribute of the model represents a database field.
	Once we write Model class, we have to generate the corresponding SQL Code. For this, we have to use makemigrations command.
	
	$py manage.py makemigrations 

	After generating sql code, we have to execute that sql code to create table in database. For this, we have to use migrate command.
	
	$py manage.py migrate
7)admin.py
	We can register our models in this file. Django will use these models with Django admin interface.
8)create superuser to login in admin interface
	We can create super user with the following command by providing username, mailid, password. 
	$py manage.py createsuperuser 
	We can login to admin interface.Start the server and login to admin interface using the created credentials. 
	$py manage.py runserver 
	Open the following in browser: http://127.0.0.1:8000/admin/
9)Views.py
	A view function, is a Python function that takes a Web request and returns a Web response. 
	This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image. 
10)serializers.py
	Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.	
11)Quit the server by using ctrl+c