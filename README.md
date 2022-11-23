# Restaurant WTTD

This project was idealized by the members of the WTTD course in order to experience the realization of a real system together.
### Virtual environment

    python -m venv venv

Linux:

    source venv/bin/activate

Windows:

    source venv\script\activate

### Install

    pip install -r requirements.txt

Then run the commands to create the database.

    python manage.py makemigrations
    python manage.py migrate

With the database created, create a super user for django administration.
It will ask for username, password and email.

    python manage.py createsuperuser

With the superuser created, simply run the project.

    python manage.py runserver