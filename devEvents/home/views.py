from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.http import HttpResponse
from event.models import Event
from event.forms import AddEventForm

def home(request):
    events=Event.objects.all()
    params={'events':events}
    return render(request,"home/home.html",params)

def about(request):
    return render(request,"home/about.html")

def search(request):
    return render(request,"home/search.html")

def addEvent(request):
    if request.method=='POST':
        title=request.POST['title']
        author=request.POST['author']
        slug=request.POST['slug']
        start_time=request.POST['start_time']
        end_time=request.POST['end_time']
        description=request.POST['description']
        content=request.POST['content']
        if len(request.FILES):
            image=request.FILES['image']
        else:
            image=NULL
        event=Event(title=title,author=author,slug=slug,start_time=start_time,end_time=end_time,description=description,content=content,image=image)
        event.save()
        return render(request,'home/home.html')
    else:
        form=AddEventForm()
        context={'form':form}
        return render(request,"home/addEvent.html",context)

