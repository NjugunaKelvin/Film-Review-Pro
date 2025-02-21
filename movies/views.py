from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)    
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', 
        {'searchTerm' : searchTerm, 'movies' : movies})


def about(request):
    return HttpResponse('<h1>About Page<h1>')

def detail(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'detail.html',
        {'movie' : movie })

def createReview(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == "GET":
        return render(request, 'createReview.html', {'form' : ReviewForm(), 'movie' : movie})
    
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('details', newReview.movie.id)
        except ValueError:
            return render(request, 'createReview.html', {'form' : ReviewForm(), 'error' : 'Bad data Passed in'})