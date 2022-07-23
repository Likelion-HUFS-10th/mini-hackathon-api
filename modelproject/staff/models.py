from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    image = models.URLField()
