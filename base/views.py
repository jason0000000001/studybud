from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.


def home(request):
    return HttpResponse('Home Page')


def room(request):
    return HttpResponse('ROOM')