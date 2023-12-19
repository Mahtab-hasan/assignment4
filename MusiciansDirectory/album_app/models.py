from django.db import models

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
