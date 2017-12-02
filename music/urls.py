from django.conf.urls import url
from . import views
"""在本地目录找有叫view 或者 views 的model文件"""
app_name = 'music'

urlpatterns = [
    # music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^player/$', views.detail, name='player'),
    # music/12/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #-------song---------

    # music/song/2/4
    url(r'^song/(?P<fk>[0-9]+)/(?P<pk>[0-9]+)/$', views.DetailSongView.as_view(), name='song'),

    # music/song/2/add
    url(r'^song/(?P<fk>[0-9]+)/add/$', views.SongCreate.as_view(), name='song-add'),

    # music/song/delete
    url(r'^song/(?P<fk>[0-9]+)/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),


    #------album-------
    # music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # music/album/2/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
