from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here

from datetime import datetime

from django.template import Template,Context
 
def Inicio(request):
    return render (request,'control/inicio.html')
