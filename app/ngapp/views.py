from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,redirect
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
from django.db.models import Avg, Count




# Create your views here.

def index(request):
    cars = []
    avg = Car.objects.annotate(avg_rate=Avg('rates__grade')).values().order_by('-id')
    if request.method == 'POST' :
        form = NewCarForm(request.POST or None)
        if form.is_valid():
            mark = form.cleaned_data['mark']
            usermodel = form.cleaned_data['model']
            BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{}?format=json".format(mark)
            response = requests.get(BASE_URL)
            data_cars = response.text
            data =json.loads(data_cars)
            
            for model in data['Results']:
                if model['Model_Name'].lower() == usermodel.lower():
                    car_to_add = form.save(commit=False)
                    messages.success(request, 'Car has been added to our data base')
                    car_to_add.save()
                    cars.append(car_to_add)
                    form = NewCarForm() 
                else:
                    pass
            if cars.__len__() == 0 :
                messages.warning(request, 'We cant find car like that ')                                   
    else :
        form = NewCarForm() 

    stuff_for_frontend = { 
        'form' : form ,
        'avg' : avg,
         }
        
    return render(request, 'ngapp/home.html',stuff_for_frontend)

def rate(request,pk):
    car = get_object_or_404(Car,pk=pk)
    cars = Car.objects.all().count()
    form = NewRateForm(request.POST or None)
    if form.is_valid():
        rate = request.POST.get('grade')
        rating = Rate.objects.create(grade=rate, car=car)
        rating.save()
        return redirect('index')
    else : 
        form = NewRateForm()

    stuff_for_frontend = {
        'car' : car,
        'form' : form,
    }
    
    return render(request, 'ngapp/rate.html', stuff_for_frontend)

def popular(request):
    number_of_rates = Car.objects.annotate(rate_count=Count('rates')).values().order_by('-id')

    return render(request,'ngapp/popular.html',{'number_of_rates' : number_of_rates})

