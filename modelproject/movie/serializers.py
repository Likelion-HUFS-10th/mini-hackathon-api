from rest_framework import serializers
from .models import *
from staff.models import * 

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'role', 'image', 'movie']
    
class CommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'movie', 'body']
        read_only_fields = ['id']

class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body']
        read_only_fields = ['id']

class MovieSerializer(serializers.ModelSerializer):
    staffs = StaffSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id']
