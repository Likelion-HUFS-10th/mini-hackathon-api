from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path("movielist/", init_db),
    path('<int:pk>/', detail, name="detail"),
]
