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
* Add functionality to change scoring in the UI
* Add users
* Add dynamic scoring for users
* Set up a hot deployment system

#### The site is currently [live](http://prospector.kayra.co.uk/) but may not reflect the latest code.

![alt text](http://kayra.co.uk/resources/images/prospector.png "Front page")
![alt text](http://kayra.co.uk/resources/images/prospector_list.png "Site list page")
![alt text](http://kayra.co.uk/resources/images/prospector_detail.png "Site inspect page")
