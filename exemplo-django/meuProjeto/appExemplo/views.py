from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def exemplo(request):
    return HttpResponse('<h1>Olá TD01</h1>')