# New project

> django-admin startproject bulletproof_ecommerce
> python manage.py runserver

# Create github new repo

bulletproof_ecommerce

> echo "# bulletproof_ecommerce" >> README.md

create .gitignore file for a dajango project

> git init
> git add \*
> git commit -m "first commit"
> git branch -M main
> git remote add origin https://github.com/codecrafteroot/bulletproof_ecommerce.git
> git push -u origin main

# create virtual env

> python -m venv venv
> activate it
> .\venv\Scripts\activate
> install deps and update pip
> pip install django
> python.exe -m pip install --upgrade pip
> create req file and push deps
> pip freeze > requirements.txt
> every time you make modification make a commit and push

# setup vscode

- try to create vscode project settings and extensions files

# Create user skeleton

- create an apps folder and inside we gonna create our apps

> django-admin.exe startapp accounts
> django-admin.exe startapp authentication

# create a new user model

- we restructure our app (models.py -> models foler , views.py -> views folder)
- add apps to project.settings INSTALLED_APPS section
- set AUTH_USER_MODEL to "accounts.UserModel"

> python manage.py makemigrations
> python manage.py migrate
> python.exe .\manage.py runserver

# create a superuser

> python.exe .\manage.py createsuperuser

- add UserModel to admin site panel
- visit Django site administration

# Start the development server

> python.exe .\manage.py runserver

# Enter the admin site

http://localhost:8000/admin/

# create auth app

install django-allauth package and configure it
[Issue] connecting with different Oauth same email !
