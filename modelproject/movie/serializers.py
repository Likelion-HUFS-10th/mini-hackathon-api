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