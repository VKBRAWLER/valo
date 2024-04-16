CMD used
virtualenv vtest
vtest/Scripts/activate
django-admin startproject testproject .
python manage.py runserver => runs the server
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser => able to use admin credentials
python manage.py startapp home
pip install djangorestframework
python manage.py startapp api