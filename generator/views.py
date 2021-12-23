from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def username(request):
    theusername = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    
    length =int(request.GET.get('length')) 

    for i in range(length):
        theusername += random.choice(characters)
    return render(request,'generator/username.html', {'username':theusername})


def about(request):
    return render(request,'generator/about.html')