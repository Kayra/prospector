# Prospector

### A web application that scrapes a website and provides relevant detailed information regarding it's Search Engine Optimisation.

#### Installation

Ensure you have virtualenv and postgres installed on your system.

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python db_create.py
    python run.py

#### Todo

* Display the data better on site inspect
* Make the spidering more robust
* Add threading for spidering
* Add users
* Add dynamic scoring for users
* Set up a hot deployment system
