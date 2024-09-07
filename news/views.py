from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    menu = ['Home', 'About', 'Contact', 'Settings']
    return render(request, 'news/home.html', {'title': 'Home', "menu":menu })

def about(request):
    menu = ['Home', 'About', 'Contact', 'Settings']
    return render(request, 'news/about.html',{'title': 'About', "menu":menu})

def contact(request):
    menu = ['Home', 'About', 'Contact', 'Settings']
    return render(request, 'news/contact.html',{'title': 'Contact', "menu":menu})


