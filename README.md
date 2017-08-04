# Prospector

### A web application that scrapes a website and provides relevant detailed information regarding it's Search Engine Optimisation.


#### Installation

Ensure you have virtualenv and postgres installed on your system. Also create a database with the [correct credentials](https://github.com/Kayra/prospector/blob/master/config.py#L4).

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py db_create
    python manage.py runserver

#### Todo

* Fix bug: https://www.rachelzarkhosh.com/ => http://https://www.rachelzarkhosh.com/
* Implement clear messaging (flash() => bootstrap)
* Link to robots.txt and sitemap.xml when present
* Make the spidering more robust
* Add threading for spidering
* Set up continuous integration

#### The site is currently [live](http://prospector.kayra.co.uk/) but may not reflect the latest code.

![alt text](http://kayra.co.uk/resources/images/prospector.png "Front page")
![alt text](http://kayra.co.uk/resources/images/prospector_list.png "Site list page")
![alt text](http://kayra.co.uk/resources/images/prospector_detail.png "Site inspect page")
