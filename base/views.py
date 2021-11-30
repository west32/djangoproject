from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q



# rooms= [
#     {'id':1, 'name':'lets learn python!'},
#     {'id':2, 'name':'Design with me !'},
#     {'id':3, 'name':'Fronend Devs!'},
# ]

def home(request):
    q= request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms= Room.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains =q)
        )
    topics = Topic.objects.all()
    room_count= rooms.count()
    context= {'rooms': rooms,'topics': topics, 'room_count':room_count }
    return render(request, 'base/home.html',context)

def room(request,pk):
   
    room = Room.objects.get(id=pk)
    context = {'room': room }
    return render(request, 'base/room.html',context)



def createRoom(request):
    form= RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'base/room_form.html',context)

def deleteRoom(request,pk):
    room= Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


def sztoki(request):
    return render(request, 'base/sztoki.html')

def tokyo(request):
    return render(request, 'base/tokyo.html')


# Create your views here.
