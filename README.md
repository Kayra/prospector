# Prospector

**A web application that scrapes a website and provides relevant detailed information regarding its Search Engine Optimisation.** This was originally built to automate the manual prospecting work an SEO team did to find local clients for potential SEO business.

(I did a partial resurrection of this application in 2023 and didn't want to spend a huge amount of time fixing something no one cares about, hence the hacky code patch in the installation process. Shoot me a message if you're interested in this project and I can implement a more reasonable fix).

## Design

![UI design](docs/screenshot_1.png)

![UI design](docs/screenshot_2.png)

![UI design](docs/screenshot_3.png)

![UI design](docs/screenshot_4.png)

## Set up and Installation

**Technologies as of 16/01/23:**

* Python 3.10.6
* psql (PostgreSQL) 14.5 (Homebrew)

### Database Set up

In Psql run:

```sql
CREATE USER prospector WITH ENCRYPTED PASSWORD 'password';
CREATEDB prospector;
```

### Unix installation

In the root directory run:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py db_create

### Code patch

**Run this after installation and before starting the server.**

This is required to make packages that are designed for Python 2 work on Python 3. 

In the root directory run:

```bash
cp ./patch_files/forms.py ./venv/lib/python3.10/site-packages/flask_user/forms.py
cp ./patch_files/__init__.py ./venv/lib/python3.10/site-packages/flask_script/__init__.py
```

## Helpful commands

To **start the server**, ensure you are in the virtualenv and in the root directory run:

```bash
python manage.py runserver
```

To **run rests**, ensure you are in the virtualenv and in the root directory run:

    nosetests
