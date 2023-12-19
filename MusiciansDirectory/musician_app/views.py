from django.shortcuts import render,get_object_or_404, redirect
from .models import Musician
from .forms import MusicianForm
from album_app.forms import AlbumForm

def home(request):
    musicians = Musician.objects.all()
    album_form = AlbumForm()
    return render(request, "musician_app/music.html", {'musicians': musicians,'album_form':album_form})

def create_musician(request):
    if request.method =="POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("musician_home")
        
    else:
        form = MusicianForm()

    return render(request,'musician_app/create_musician.html',{"form":form})

def edit_musician(request,musician_id):
    musician = get_object_or_404(Musician,id=musician_id)

    if request.method == "POST":
        form = MusicianForm(request.POST,instance= musician)
        if form.is_valid():
            form.save()
            return redirect("musician_home")
    else:
        form = MusicianForm(instance= musician)
    return render(request,'musician_app/edit_musician.html',{"form":form,'musician_id':musician_id})

def delete_musician(request,musician_id):
    musician = get_object_or_404(Musician,id=musician_id)
    if request.method =="POST":
        musician.delete()
        return redirect("musician_home")
    return render(request, "musician_app/delete_musician.html",{"musician": musician})