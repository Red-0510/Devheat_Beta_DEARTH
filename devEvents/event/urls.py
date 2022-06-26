from django.contrib import admin
from django.urls import path
from event import views
urlpatterns = [
    path('',views.allEvents,name='allEvents'),
    path('allEvents/',views.allEvents,name="allEvents"),
    path('futureEvents/',views.futureEvents,name="futureEvents"),
    path('currentEvents/',views.currentEvents,name="currentEvents"),
    path('pastEvents/',views.pastEvents,name="pastEvents"),
    path('<str:slug>',views.eventPage,name="eventPage"),
]
