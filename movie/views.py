from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hola Profe, gracias por el tutorial!</h1>')

# Create your views here.
