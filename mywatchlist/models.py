from django.db import models

class MyWatchList(models.Model):
    watched = models.CharField(max_length=5)              # yes/no
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
