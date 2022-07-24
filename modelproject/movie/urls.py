from django.urls import path
from .views import *

app_name = 'movie'

urlpatterns = [
    path('<int:pk>/', detail, name="detail"),
]