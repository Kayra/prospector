# Prospector

### A web application that scrapes a website and provides relevant detailed information regarding it's Search Engine Optimisation.

#### Installation

Ensure you have virtualenv and postgres installed on your system. Also create a database with the [correct credentials](https://github.com/Kayra/prospector/blob/master/config.py#L4).

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage db_create
    python manage runserver

#### Todo

* Display the data better on site inspect
* Make the spidering more robust
* Add threading for spidering
* Add users
* Add dynamic scoring for users
* Set up a hot deployment system
