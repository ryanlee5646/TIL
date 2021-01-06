from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_id = models.IntegerField(blank=True)
    title_kr = models.CharField(max_length=200) # 한국어 제목
    title_en = models.CharField(max_length=200) # 영어 제목
    poster_path =  models.TextField(blank=True) # 영화 포스터
    overview= models.TextField(blank=True) # 개요
    release_date = models.TextField(blank=True) # 개봉날짜
    genres = models.ManyToManyField(Genre, related_name="movies") # 장르와 1:N관계 (영화 하나에 장르 여러개)
    vote_count = models.IntegerField(blank=True)
    vote_average = models.FloatField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies',blank=True)
    def __str__(self):
        return self.title_kr
    
class Comment_Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)

