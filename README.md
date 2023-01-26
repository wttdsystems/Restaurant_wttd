# Restaurant WTTD

This project was idealized by the members of the WTTD course in order to experience the realization of a real system together.

## Links
 - [Trello](https://trello.com/b/bDtpk8Jm/projeto-restaurante)
 - [Document](https://docs.google.com/document/d/1Ja4pKlef_GNj4axUTOpFCGb5aE5QG-XIfEvZTobEAVY/edit?userstoinvite=geancarlosgava@gmail.com)


## Virtual environment

    python -m venv venv


Linux:

    source venv/bin/activate

Windows:

    source venv\script\activate

## Install

    pip install -r requirements.txt

Then run the commands to create the database.

    python manage.py makemigrations
    python manage.py migrate

With the database created, create a super user for django administration.
It will ask for username, password and email.

    python manage.py createsuperuser

With the superuser created, simply run the project.

    python manage.py runserver

## Development

```bash
pip install -r requirements-dev.txt
```

### Formatting

```bash
make fmt
```

or

```
isort Restaurant core
black Restaurant core
```

### Linter

```bash
make linter
```
or

```bash
pflake8
```

## Run tests

```bash
make tests
```
or

```bash
pytest
```
