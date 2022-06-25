from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('addEvent/',views.addEvent,name="addEvent"),
]
