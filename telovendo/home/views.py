from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bienvenida(request):
    return HttpResponse("<h1 style='color:red;'>Bienvenido a te lo vendo</h1>")

