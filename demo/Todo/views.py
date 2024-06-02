from django.shortcuts import render,HttpResponse # type: ignore
from .models import TodoItem

# Create your views here.

def index(request):
    return HttpResponse("Hello friends")

def todo_list(request):
    return render(request,"todo.html",{
        "todos":TodoItem.objects.all(),
        "title":"TODOAPP"
    })

places = [
    {"id":1, "name":"Mysore"},
   { "id":2, "name":"Gadhag"},
   { "id":3, "name":"Davanagere"},
   { "id":4, "name":"Nanjangud"},
   { "id":5, "name":"Chamarajanaga"}   
]
    


def getPalces(request):
    return render(request,"index.html",{
        "places": places,
        "title":"my template",
        "header":"FAMOUS PLACES"
    })


def room(request, pk):
    room = None
    for place in places:
        if place['id'] == (pk):
            room = place['name']
    return render(request,"room.html",{
        "place":room
    })
