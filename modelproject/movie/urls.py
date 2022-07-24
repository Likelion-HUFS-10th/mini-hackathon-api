from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path("movielist/", init_db),
    path('<int:pk>/', detail, name="detail"),
    path('comments/<int:movie_id>', get_movie_comments),
    path('comment', post_movie_comment),
    path('comment/delete', delete_movie_comment)
]