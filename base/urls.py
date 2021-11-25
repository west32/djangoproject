from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name="home"),
    path('room/<str:pk>/',views.room, name="room"),
    path('sztoki/', views.sztoki, name="sztoki"),
    path('sztoki/tokyo/', views.tokyo, name="tokyo")
]