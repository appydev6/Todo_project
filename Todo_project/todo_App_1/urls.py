from django.contrib import admin
from django.urls import include, path
from . views import hello_world

urlpatterns = [
    path('index/', hello_world),
]