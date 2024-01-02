from django.db import models
from musician.models import Musician
# Create your models here.
class Reting(models.Model):
    rating = models.CharField(max_length = 5)

    def __str__(self):
        return self.rating


class Album(models.Model):
    album_name = models.CharField(max_length = 50)
    album_release_date = models.DateTimeField(auto_now_add = True)
    name = models.ForeignKey(Musician, on_delete = models.CASCADE)
    rating_between = models.ForeignKey(Reting, on_delete = models.CASCADE)

    def __str__(self):
        return self.album_name
