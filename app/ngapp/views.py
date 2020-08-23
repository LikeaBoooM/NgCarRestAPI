from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
from . forms import NewCarForm, NewRateForm
from . models import Car, Rate
from bs4 import BeautifulSoup
from django.contrib import messages
import requests
import json



# Create your views here.

def index(request):
    form = NewCarForm(request.POST or None)
    status = False
    object_first = Car.objects.first()
    dane = []
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
                Car1 = form.save()
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
        'dane' : Car.objects.all(),
         }
        
    return render(request, 'ngapp/home.html',stuff_for_frontend)

def rate(request,pk):
    car = get_object_or_404(Car,pk=pk)
    cars = Car.objects.all().count()
    print(cars)
    form = NewRateForm(request.POST or None)
    if form.is_valid():
        rate = request.POST.get('grade')
        rating = Rate.objects.create(grade=rate, car=car)
        rating.save()
        return HttpResponse('Thanks for voting')
    else : 
        form = NewRateForm()

    stuff_for_frontend = {
        'car' : car,
        'form' : form,
    }
    
    return render(request, 'ngapp/rate.html', stuff_for_frontend)
