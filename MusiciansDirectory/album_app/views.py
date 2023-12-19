from django.shortcuts import render,get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm
from musician_app.models import Musician

def home(request):
    albums = Album.objects.all()
    return render(request, "album_app/album.html", {'albums': albums})

def create_album(request):
    form = AlbumForm(request.POST)

    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect("album_home")
        
    total_musicians = Musician.objects.count()

    return render(request,'album_app/create_album.html',{"form":form,"total_musicians":total_musicians})

def edit_album(request,album_id):
    album = get_object_or_404(Album,id=album_id)

    if request.method == "POST":
        form = AlbumForm(request.POST,instance= album)
        if form.is_valid():
            form.save()
            return redirect("album_home")
    else:
        form = AlbumForm(instance=album)
    return render(request,'album_app/edit_album.html',{"form":form,"album_id":album_id})
        
def delete_album(request,album_id):
    album = get_object_or_404(Album,id=album_id)
    if request.method =="POST":
        album.delete()
        return redirect("album_home")
    return render(request, "album_app/delete_album.html",{"album": album})