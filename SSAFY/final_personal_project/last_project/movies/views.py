from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment_Score, Genre
from .forms import CommentScoreForm
from django.http import JsonResponse
from django.views.generic.edit import FormView
import json, requests


# from .serializers import MovieSerializer, CommentSerializer, ScoreSerializer



def movie_list(request):
    movies = Movie.objects.all()
    overview = ''
    return render(request, 'movies/list.html', {'movies':movies, 'overview':overview})

    
def movie_detail(request,movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    comment_score_form = CommentScoreForm()
    res = requests.get(f'https://api.themoviedb.org/3/movie/{movie.movie_id}/credits?api_key=fbba0ab051a2676aeb15855cbf738aed')
    actors = res.json()['cast'][0:6] # 배우 정보가 담겨있는 배열
    
    return render(request,'movies/detail.html',{'movie':movie, 'comment_score_form':comment_score_form, 'actors': actors })

    
@login_required # 로그인해야 댓글 작성 가능
@require_POST # POST요청으로 들어와야 실행
def comments_create(request, movie_id):
    comment_score_form = CommentScoreForm(request.POST)
    if comment_score_form.is_valid():
      
        comment_score = comment_score_form.save(commit=False)
        comment_score.user = request.user
        comment_score.movie_id = movie_id
        comment_score.save()
    new_score = comment_score.score
    movie = get_object_or_404(Movie,id=movie_id)
    total = movie.vote_count * movie.vote_average
    movie.vote_count+=1
    movie.vote_average = round((total+new_score)/movie.vote_count,2)
    movie.save()    
    return redirect('movies:detail', movie_id)

@require_http_methods(['GET','POST'])
def comments_delete(request, movie_id, comment_score_id):
    comment_score= get_object_or_404(Comment_Score, id=comment_score_id)
    if comment_score.user != request.user: # 댓글적은 사람과 로그인한 사람이 다르다면 삭제불가
        return redirect('movies:list')
    comment_score.delete()
    movie = get_object_or_404(Movie, id=movie_id)
    total = (movie.vote_count * movie.vote_average) - comment_score.score 
    movie.vote_count -= 1
    movie.vote_average = round(total/movie.vote_count,2)
    movie.save()
    return redirect('movies:detail', movie_id)
    
@login_required
def like(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    print(request.user)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        liked=False
    else:
        movie.like_users.add(request.user)
        liked=True
    return JsonResponse({'liked':liked,'count':movie.like_users.count()})
    
def search(request):
    keyword = request.GET.get('keyword')
   
    movies=Movie.objects.filter(title_kr__icontains=keyword)
  
    return render(request, 'movies/search.html', {'movies':movies})
    
def top(request):
    movies=Movie.objects.filter(vote_count__gt=1000).order_by('-vote_average')[:10]
    return render(request,'movies/top.html',{'movies':movies})

def selfsearch(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    return render(request,'movies/selfsearch.html',{'genres':genres, 'movies':movies})
def selftop(request):
    year = request.GET.get('year')
    genrename = request.GET.get('genrename')
    point = request.GET.get('point')
    people = request.GET.get('people')
    movies = Movie.objects.filter(vote_count__gt=people, vote_average__gt=point).order_by('-vote_average')[:10]
    return render(request,'movies/selftop.html',{'movies':movies})