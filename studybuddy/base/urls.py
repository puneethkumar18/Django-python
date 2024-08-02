from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('room/<str:pk>',views.room,name="room"),
    path('create-room/',views.createRoom,name="createRoom"),
    path('update-room/<str:pk>',views.updateRoom,name="updateRoom"),
    path('delete-room/<str:pk>',views.deleteRoom,name="deleteRoom"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="registerUser"),
    path('delete/<str:pk>',views.deleteMessage,name="deleteMessage"),
    path('user-profile/<str:pk>/',views.userProfile,name="user-profile"),
    path('update-user/',views.updateUser,name="updateUser"),
    path('topics-page/',views.topicsPage,name="topicsPage"),
    path('activities/',views.activityPage,name="activityPage"),
    
]


