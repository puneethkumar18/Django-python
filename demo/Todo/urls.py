from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("list",views.todo_list,name="todo_list"),
    path("place",views.getPalces,name="getPlaces"),
    path("room/<int:pk>",views.room,name="room")
]
