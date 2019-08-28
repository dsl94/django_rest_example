from django.db import models


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
