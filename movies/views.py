from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name' : 'Vin'})


def about(request):
    return HttpResponse('<h1>About Page<h1>')
    