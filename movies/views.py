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
    reviews = Review.objects.filter(movie = movie)
    return render(request, 'detail.html',
        {'movie' : movie, 'review' : reviews})

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
            return redirect('detail', newReview.movie.id)
        except ValueError:
            return render(request, 'createReview.html', {'form' : ReviewForm(), 'error' : 'Bad data Passed in'})
        

def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user = request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html', {'review' : review, 'form' : form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'updatereview.html', {'review' : review, 'form' : form, 'error' : 'Bad Data in the Form'})
        



def deletereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    review.delete()
    return redirect('detail', review.movie.id)