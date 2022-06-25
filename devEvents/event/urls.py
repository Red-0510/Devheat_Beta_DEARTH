from django.contrib import admin
from django.urls import path,include
from event import views
urlpatterns = [
    path('',views.home,name='home'),
    path('future-events/',views.future_events,name="future_events"),
    path('current-events/',views.current_events,name="current_events"),
    path('past-events/',views.past_events,name="past_events"),
]
