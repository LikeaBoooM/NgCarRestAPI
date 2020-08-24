from django.urls import path

from . import views

urlpatterns = [
    path('cars/', views.index, name='index'),
    path('rates/<int:pk>', views.rate, name='rates'),
    path('popular/', views.popular, name='popular'),

]