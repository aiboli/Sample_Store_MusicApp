from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
"""Album 继承自 models.Model"""


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    """展示自己在colsol里面"""
    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    """on_delete = models.cascade 意思是如果对应的foreignkey的model被删除了 那么 对应得song也会被删除"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    song_file = models.FileField()

    def get_absolute_url(self):
        return reverse('music:song', kwargs={'fk': self.album.pk, 'pk': self.pk, })

    def __str__(self):
        return self.song_title
