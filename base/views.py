from django.shortcuts import render
from django.http import HttpResponse


rooms= [
    {'id':1, 'name':'lets learn python!'},
    {'id':2, 'name':'Design with me !'},
    {'id':3, 'name':'Fronend Devs!'},
]

def home(request):
    context= {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request):
    return render(request, 'base/room.html')

def sztoki(request):
    return render(request, 'base/sztoki.html')

def tokyo(request):
    return render(request, 'base/tokyo.html')


# Create your views here.
