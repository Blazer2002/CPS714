# CPS714 - Loyalty Points And Rewards System

This subproject is a part of a larger project - EcoFix Solutions: Client Engagement Web Portal.

This project will use the Django Stack which is Python, Django, and MySQL. \
The frontend will be using Django REST API (DRF) with React.js which uses JavaScript.

## Frontend Setup (React.js)

Install Node.js and npm. Visit https://nodejs.org/en to install Node.js. \
Make sure that you are in version 14.x or newer.

Note that npm is a command which comes with the Node.js.

### Available Scripts

In the project directory, you can run:

#### `npm install`

Installs everything the project needs in the `node_modules` folder, creating it if it's not existing already. \
The installed dependancies when running `npm install` are stated in the Frontend directory as `package.json`.

You can state which `package.json` to apply when running `npm install <package-name>` where `package-name` is  \
the specified package JSON file.

#### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.


## Backend Setup (Django)

Note: Make sure you are using a virtual environment.

Install the following packages:\
`pip install django`\
`pip install djangorestframework`\
`pip install django-cors-headers`

Run the backend server:\
`python manage.py runserver`

Create an app in the project:\
`python manage.py startapp <app-name>` where `app-name` is replaced for what you want to name your app.\
For this case, I named the app `lprs`.\

Find the config, go to `<app-name>/apps.py`. You will see a class named `<app-name>Config`.\
Add the app config to `INSTALLED_APPS` inside of `settings.py`.\
For this case, the added app config is `lprs.apps.LprsConfig`.\

Follow the repo files to edit your `urlpatterns` in project `urls.py`:\
Do the same for `urls.py` in your apps folder.\
Remember to change the `<app-name>` for both `urls.py`.\

Move on to database setup when you are done with backend setup.\

## Database Setup (mySQL)

Note: Make sure you are using a virtual environment.

Install the following packages within the `Backend` directory:\
`pip install mysqlclient`

mySQL Connection:\
`pip install python-dotenv` to have environmental varaibles for credentials.\
Add a `.env` file and store your credentials. (Do not share .env file)\
Format of variables are `DB_<VAR> = <value>`.\
Store this file at `Backend/rewards_backend/.env`.\
This will modify the `settings.py` file for `DATABASES = {...}` to have your local database credentials.


### Available Scripts

#### `python manage.py inspectdb > models.py`
Auto-generate the models in order to preprare for migration.\
Open the file in application `Notepad` and save the file with encoding `UTF-8`.\
Replace `models.py` within your apps folder with the newly generated models.py file.\

#### `python manage.py makemigrations`
Create new migrations based on the changes make to your models.\
Follow the instuctions in `models.py` to fix any errors with the generated model.\
There will be some extra generated models not related to the database. Please delete those models.\
Don't worry about the `primary_key=True` issue since Django will add an IntegerField for the primary key.\
Refer to the database files for the structure of the database.\

#### `python manage.py migrate`
Apply/Unapply migrations.

#### `python manage.py showmigrations`
Show migrations and their status.

## Online Setup Guides:

### Backend
https://medium.com/@sp.techwriter/create-cms-react-django-api-and-mysql-database-for-beginners-a15e628035c2

https://medium.com/@sinturana07/create-crud-operation-using-django-inbuilt-form-and-mysql-using-the-database-in-project-chapter-6-968a907dcb9a
