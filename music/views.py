"""generic view"""
from django.views import generic
from .models import Album, Song
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.base import RedirectView
from .forms import UserForm
from django.shortcuts import reverse


def detail(request):

    return render(request, 'music/player-old.html')


class DetailSongView(generic.DetailView):

    model = Song
    template_name = 'music/song_success.html'


class IndexView(generic.ListView):

    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):

    model = Album
    template_name = "music/detail.html"


class SongCreate(CreateView):
    model = Song
    fields = [
        'album',
        'file_type',
        'song_title',
        'song_file',
    ]


class SongDelete(DeleteView):

    model = Song

    def get_success_url(self):
        song = self.object
        return reverse_lazy('music:detail', kwargs={'pk': song.album.pk})
    # success_url = reverse_lazy('music:detail', kwargs={'pk': model.album.id})


class AlbumCreate(CreateView):
    model = Album
    fields = [
        'artist',
        'album_title',
        'genre',
        'album_logo'
    ]


class AlbumUpdate(UpdateView):
    model = Album
    fields = [
        'artist',
        'album_title',
        'genre',
        'album_logo'
    ]


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'
    # display blank form

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form data

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})
