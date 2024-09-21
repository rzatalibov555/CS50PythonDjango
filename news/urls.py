from django.urls import path

from .views import *

urlpatterns = [
    path('',index, name="home"),
    path('contact/',contact, name="contact"),
    path('news_detail/',detail, name="detail"),
    # path('news_detail/<int:id>',detail, name="detail"),
    path('category/<int:cat_id>',show_category, name="category")
    
]