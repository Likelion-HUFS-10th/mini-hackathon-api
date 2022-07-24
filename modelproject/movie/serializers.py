from rest_framework import serializers
from .models import *

class CommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = ['id', 'author', 'movie', 'body']
        read_only_fields = ['id']

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = ['id', 'body']
        read_only_fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title_kor','title_eng','poster_url',
                  'rating_aud','rating_cri','rating_net',
                  'genre','showtimes','release_date','summary']
        read_only_fields = ['id']