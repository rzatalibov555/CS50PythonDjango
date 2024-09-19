from django.shortcuts import render
from django.http import HttpResponse

from news.models import News

# Create your views here.

def index(request):
    
    context = {
        "title": 'Home',
        "posts": News.objects.all()
    }
    return render(request, 'news/index.html', context)

def contact(request):
    context = {
        "title": 'Contact',
    }
    return render(request, 'news/contact.html',context=context)


def detail(request):
    menu = ['Home', 'About', 'Contact', 'Settings']
    return render(request, 'news/single-page.html',{'title': 'Contact', "menu":menu})


