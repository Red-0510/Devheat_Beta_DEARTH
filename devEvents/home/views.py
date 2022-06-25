from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home/home.html")

def about(request):
    return render(request,"home/about.html")

def search(request):
    return render(request,"home/search.html")

def addEvent(request):
    return render(request,"home/addEvent.html")

