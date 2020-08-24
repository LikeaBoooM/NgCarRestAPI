from bs4 import BeautifulSoup
import requests
import json

def checkModelifExists(model):
    BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/honda?format=json"
    response = requests.get(BASE_URL)
    Model = model
    data_cars = response.text 
    xmlSoup = BeautifulSoup(data_cars, 'html.parser')
    found = False
    for line in data_cars:
        print(line)
        if Model in line:
            found = True
            break


def checkModelifExists1(model1):
    BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/volkswagen?format=json"
    response = requests.get(BASE_URL)
    data_cars = response.text
    data =json.loads(data_cars)
    for model in data['Results']:
        if model['Model_Name'].lower() == model1.lower():
            print(True)
        else:
            print(False)

checkModelifExists1('GOLF III')



