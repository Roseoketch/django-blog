from django import urls
from django.urls import path  
from . import views

urlpatterns = [

    path('',views.post, name='post' )

]