from django.shortcuts import render
from django.http import HttpResponse
from event.models import Event
from django.utils import timezone


def allEvents(request):
    events=Event.objects.all()
    future_events=[]
    past_events=[]
    current_events=[]
    now=timezone.now()
    for event in events:
        if (event.start_time>now):
            future_events.append(event)
        elif (event.end_time>now and event.start_time<=now):
            current_events.append(event)
        else:
            past_events.append(event)
    params={'future_events':future_events,'current_events':current_events,'past_events':past_events}
    return render(request,"event/allEvents.html",params)
    
def futureEvents(request):
    now=timezone.now()
    events=Event.objects.all()
    future_events=[]
    for event in events:
        if (event.start_time>now):
            future_events.append(event)
    params={'future_events':future_events}
    return render(request,"event/futureEvents.html",params)

def currentEvents(request):
    now=timezone.now()
    events=Event.objects.all()
    current_events=[]
    for event in events:
        if (event.start_time<=now and event.end_time>now):
            current_events.append(event)
    params={'current_events':current_events}
    return render(request,"event/currentEvents.html",params)

def pastEvents(request):
    now=timezone.now()
    events=Event.objects.all()
    past_events=[]
    for event in events:
        if (event.end_time>now):
            past_events.append(event)
    params={'past_events':past_events}
    return render(request,"event/pastEvents.html",params)

def eventPage(request,slug):
    event=Event.objects.filter(slug=slug).first()
    params={'event':event}
    return render(request,"event/eventPage.html",params)