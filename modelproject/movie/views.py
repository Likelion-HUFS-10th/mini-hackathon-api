from django.shortcuts import render, redirect
from .models import Movie
from staff.models import Staff
import requests
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def init_db(request):
    url = "https://46f95f3a-8415-41f5-8848-c23892b059bb.mock.pstmn.io/movies"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        new_movie = Movie()
        new_movie.title_kor = movie['title_kor']
        new_movie.title_eng = movie['title_eng']
        new_movie.poster_url = movie['poster_url']
        new_movie.rating_aud = movie['rating_aud']
        new_movie.rating_cri = movie['rating_cri']
        new_movie.rating_net = movie['rating_net']
        new_movie.genre = movie['genre']
        new_movie.showtimes = movie['showtimes']
        new_movie.release_date = movie['release_date']
        new_movie.rate = movie['rate']
        new_movie.summary = movie['summary']
        new_movie.save()

        staffs = movie['staff']
        for staff in staffs:
            new_staff = Staff()
            new_staff.name = staff['name']
            new_staff.role = staff['role']
            new_staff.image = staff['image_url']
            new_staff.movie = new_movie
            new_staff.save()

    return redirect('')

@api_view(['GET'])
def home(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request,pk):
    try:
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

