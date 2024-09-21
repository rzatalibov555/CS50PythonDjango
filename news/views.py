from django.shortcuts import render
from django.http import HttpResponse

from news.models import News, Category

# Create your views here.

def index(request):
    posts = News.objects.all()
    cats = Category.objects.all()
    context = {
        "title": 'Home',
        "posts": posts,
        "cats" : cats,
        "cat_selected": 0,
    }
    return render(request, 'news/index.html', context)

def contact(request):
    context = {
        "title": 'Contact',
    }
    return render(request, 'news/contact.html',context=context)


def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    
    context = {
            "title": 'Category',
            "posts": posts,
            "cats": cats,
            "cat_selected": cat_id,
            
        }
    return render(request, 'news/category.html', context)



def detail(request):
    menu = ['Home', 'About', 'Contact', 'Settings']
    return render(request, 'news/single-page.html',{'title': 'Contact', "menu":menu})


