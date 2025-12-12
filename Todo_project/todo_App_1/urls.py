from django.contrib import admin
from django.urls import include, path
from . views import hello, index, bye   

urlpatterns = [
    path('index/', index),
    path('bye/', bye),
    path('hello/', hello),
]