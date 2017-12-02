
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# Create your views here.

def index(req):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return render(req, 'music/index.html', context)
    # return HttpResponse(template.render(context, req))

def detail(req, album_id):
    #try:
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id)
    return render(req, 'music/detail.html', {'album': album})

def favorite(req,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=req.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(req, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(req, 'music/detail.html', {'album': album})
