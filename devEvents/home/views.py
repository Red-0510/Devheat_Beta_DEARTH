from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("this is home")

def about(request):
    return HttpResponse("this is about")

def search(request):
    return HttpResponse("this is search")

def add_event(request):
    return HttpResponse("this is add_event")

