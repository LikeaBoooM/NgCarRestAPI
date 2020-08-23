from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
from . forms import NewCarForm
from . models import Car
from bs4 import BeautifulSoup
import requests
import json



# Create your views here.

def index(request):
    form = NewCarForm(request.POST or None)
    dane = Car.objects.all()
    status = False
    if form.is_valid():
        mark = form.cleaned_data['mark']
        usermodel = form.cleaned_data['model']
        BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{}?format=json".format(mark)
        response = requests.get(BASE_URL)
        data_cars = response.text
        data =json.loads(data_cars)
        for model in data['Results']:
            if model['Model_Name'].lower() == usermodel.lower():
                print(model['Model_Name'])
                print(usermodel)
                status = True
                dane.append(mark)
                dane.append(usermodel)
                Car = form.save()
            else:
                print(model['Model_Name'])
                print(usermodel)
        if status is True :
            return HttpResponse('Jest takie auto')
        else :
            return HttpResponse('Nie ma takiego auta')
    else :
        form = NewCarForm()
    stuff_for_frontend = { 
        'form' : form ,
        'dane' : dane, }
        
    return render(request,'ngapp/home.html',stuff_for_frontend)
