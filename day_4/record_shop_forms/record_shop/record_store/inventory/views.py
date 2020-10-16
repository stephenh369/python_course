from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventory.models import *
from inventory.forms import AlbumForm

def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            print(album)
            album.save()
            return redirect('index')
    else:
        form = AlbumForm()
        return render(request, "inventory/album_form.html", locals())