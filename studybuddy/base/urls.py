from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('room/<str:pk>',views.room,name="room"),
    path('create-room/',views.createRoom,name="createRoom"),
    path('update-room/<str:pk>',views.updateRoom,name="updateRoom"),
    path('delete-room/<str:pk>',views.deleteRoom,name="deleteRoom")
]
