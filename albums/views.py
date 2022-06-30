from django.shortcuts import render, redirect, get_object_or_404
from .models import Album

def add_album(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})

def album_detail(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})

def delete_album(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})

def edit_album(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})

def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})
