from django.shortcuts import render
from django.http import HttpResponse


def allEvents(request):
    return render(request,"event/allEvents.html")
    
def futureEvents(request):
    return render(request,"event/futureEvents.html")

def currentEvents(request):
    return render(request,"event/currentEvents.html")

def pastEvents(request):
    return render(request,"event/pastEvents.html")