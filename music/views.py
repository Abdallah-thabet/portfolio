from django.shortcuts import render
from .forms import AlbumForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Album


# Create your views here.
def home(request):
    return render(request, 'music/home.html')


def contactus(request):
    return render(request, 'music/contactus.html')


def albums_list(request):
    queryset = Album.objects.all()
    return render(request, 'music/albums_list.html', {'albums': queryset})


def album_detail(request, id=None):
    queryset = get_object_or_404(Album, id=id)
    return render(request, 'music/album_details.html', {'instance': queryset})


def AlbumCreate(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False) #* commit=False is used to save the object in the memory not in the db yet.
        instance.save()                    #? i will try to run the app without it.
        return HttpResponseRedirect('/home/albums/')
    return render(request, 'music/albums_create.html', {'form': form})#? i will try to run the app without it.


def media_error(request):
    return render(request, 'music/media_error.html')
