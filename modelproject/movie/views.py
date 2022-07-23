from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentGetSerializer, CommentPostSerializer
from .models import *

# Create your views here.
@api_view(['GET'])
def get_movie_comments(request, movie_id):
    try:
        comments = Comment.objects.get(movie__id = movie_id)
        serializer = CommentGetSerializer(comments, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except Movie.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_movie_comment(request, movie_id):
    try:
        serializer = CommentPostSerializer(data=request.data)
        movie = Movie.objects.get(pk = movie_id)
        if serializer.is_valid():
            serializer.save(author=request.user, movie = movie)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_movie_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk = comment_id)
        if comment.author == request.user:
            comment.delete()
            return Response(status = status.HTTP_200_OK)
        return Response(status = status.HTTP_403_UNAUTHORIZED)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)