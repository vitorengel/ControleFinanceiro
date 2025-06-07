from matplotlib import pandas
from django.http import HttpResponse
from django.urls import path
from .views import home


def home(request):
    return HttpResponse("<h1>Minha página inicial</h1><p>Projeto iniciado!</p>")




print("Hello World")