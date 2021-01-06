from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.TextField()
    