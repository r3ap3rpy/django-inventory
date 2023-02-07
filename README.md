### Welcome

This is a demo inventory app.

In order to use it you have to do the following.

``` bash
git clone https://github.com/r3ap3rpy/django-inventory.git
virtualenv djangoinv
djangoinv\Scripts\activate.bat
pip install django
cd django-inventory
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```