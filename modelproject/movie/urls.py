from django.urls import path, include
from .views import *

urlpatterns = [
    path('comments/<int:movie_id>', get_movie_comments),
    path('comment', post_movie_comment),
    path('comment/delete', delete_movie_comment)
]