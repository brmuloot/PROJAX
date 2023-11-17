# PROJAX

## Installation

```bash
conda create -n django
conda activate django
pip install -r requirements.txt
```

## How to create an admin account
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```
Choose you username, email adress, and your password

```bash
python manage.py runserver
```
* Add /admin/ at the end the URL
* Complete the authentication form
* Create a new post (title, date, and time)
* Save !
