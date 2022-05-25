# CP
#1/setup
$ pipenv shell
$ pipenv install django
$ pipenv install djangorestframework
#2/Create
$ django-admin startproject CP
$ django-admin startapp login
#3/Build
$ python manage.py migrate
$ python manage.py runserver
$ python manage.py makemigrations
