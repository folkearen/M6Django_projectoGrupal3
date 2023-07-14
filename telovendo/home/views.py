from django.shortcuts import render
from django.http import HttpResponse
import datetime
import locale

# Create your views here.

def bienvenida(request):
    locale.setlocale(locale.LC_TIME, 'es_ES')
    time = datetime.datetime.now().strftime('%A %d/%m/%Y %H:%M:%S').capitalize()
    return render(request, 'home/index.html', {
        'time' : time
    } )

