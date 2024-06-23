from django.shortcuts import render, redirect

# from base.templates import *
# Create your views here.

# -------start of static data

# # -----MYCODE------

# rooms = [
#     {'id': 1, 'name': 'LET lear Django'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend Developers'},
# ]

# # -----MYCODE------
# # from django.http import HttpResponse

# # -----MYCODE------
# def home(request):
#     # return HttpResponse('Home page')
#     contxt = {'rooms': rooms}
#     return render(request,template_name='base/home.html', context=contxt)


# def room(request,pk):
#     room = None
#     for i in rooms:
#         if i['id'] == int(pk):
#             room = i
#     context = {'room': room}
#         # return HttpResponse('<h1>Room page</h1>')
#     return render(request,"room.html",context)

#---end of static data

# ----- start dyanamic data fetching 

from .models import Room, Topic


def home(request):
    rooms = Room.objects.all() #query for room
    q = request.GET.get('q')
    # room = Room.objects.filter(topic__name = q)
    topics = Topic.objects.all() #query for topic in browser 
    contxt = {'rooms':rooms, 'topics':topics}
    return render(request,'base/home.html',context=contxt)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,"base/room.html",context)


from .forms import RoomForm
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'forms_room' : form}
    return render(request, "base/room_form.html",context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'forms_room':form}
    return render(request, "base/room_form.html",context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})