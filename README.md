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

## Database Setup (mySQL)

Note: Make sure you are using a virtual environment.

Install the following packages within the `Backend` directory:\
`pip install mysqlclient`

mySQL Connection:\
Modify the `settings.py` file for `DATABASES = {...}` to have your local database credentials.

Run the backend server:\
`python manage.py runserver`

Migration Command:\
`python manage.py makemigrations`\
`python manage.py migrate`
