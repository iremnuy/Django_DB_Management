# Django_DB_Management


## First things first 

create a virtualenv in root directory with 

> python3 -m venv venv 

activate the venv 

source venv/bin/activate 

then install the dependencies via 

> pip install -r requirements.txt 

your initial setup is done!

## Commands before run 
To run the mysql container in docker go to db folder with 

> cd db

and then run 

> docker-compose up --build 

this will pull the mysql image and run it, you can check the container via docker desktop or run the following cmd 

> docker ps 

then go to parent directory and then src folder

> cd ../src

run the following command to see the entitites in app/models.py in your database served in localhost:3308

> python3 manage.py makemigrations

and then 

> python3 manage.py migrate 

That's all, you should see the entities in your db now


## .gitignore 
 Please make sure that venv,mydb and environment variables are in gitignore.

## .env 

Things need to be added to env : 

please create a .env file in src folder with the following key-value pairs

# Django settings
SECRET_KEY='django-insecure-2=-_)1-!@+e4d#t&%1ztg4-5d4j(-2vfyn3k$p5rw2#jqe1%x)'
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# MySQL settings
MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=db
MYSQL_USER=root
MYSQL_PORT=3308