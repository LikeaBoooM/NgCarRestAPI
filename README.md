# NgCarRestAPI
 Recruitment task


Foobar is a Python library for dealing with word pluralization.
## Technologies
 * Python
 * Django
 * Docker 
 * Bootstrap

## Installation

Open application folder with powershell and run command below :
```shell
cd .\NgCarRestAPI\
```

```shell
docker-compose build 
```

after installing each requirement you can start python server with command : 


```shell
python manage.py runserver 
```
After that open your browser and go to http://localhost:8000/cars/

## Usage

* POST /cars

In this view, we see basic form with two fields. If we introduce corret data in both fields, application will return success message about existing car in this API https://vpic.nhtsa.dot.gov/api/ and about adding car to our data base. If We introduce wrong data, We will have wrong message returned and that means the data are wrong or in our database car with same mark and model exists.


* POST /rate

We can rate each object in our data base. We have to just click RATE in /cars view and we will be move /rate view where We will find the car we wanted to rate from site before. We see mark and model of car and many choices of rates We can give to this car.

* GET /cars

Below the form, each car is shown in table with mark, model and with their current average rate.


* GET /popular

In this view we see table with each object in our database with field called Number of Rates which means how many votes each car has.



## HEROKU

Project is deployed on Heroku 
[link](https://checkmodelofyourcar.herokuapp.com/cars/)


## Authors 

https://github.com/LikeaBoooM

