from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is home for events")
    
def future_events(request):
    return HttpResponse("this is home for future_events")

def current_events(request):
    return HttpResponse("this is home for current_events")

def past_events(request):
    return HttpResponse("this is home for past_events")