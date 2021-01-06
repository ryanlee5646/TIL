from django.shortcuts import render
from .forms import MovieForm

# Create your views here.
def create(request):
    movie_form = MovieForm()
    return render(request, 'movies/create.html', {'movie_form': movie_form})