from django.db import models
from movie.models import Movie

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image = models.URLField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

