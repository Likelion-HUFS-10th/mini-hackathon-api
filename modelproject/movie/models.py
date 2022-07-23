from django.db import models
from account.models import User

class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.URLField()
    rating_aud = models.FloatField()
    rating_cri = models.FloatField()
    rating_net = models.FloatField()
    genre = models.CharField(max_length=50)
    showtimes = models.CharField(max_length=10)
    release_date = models.CharField(max_length=50)
    rate = models.CharField(max_length=100)
    summary = models.TextField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField()