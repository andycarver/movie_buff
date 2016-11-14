from django.shortcuts import render, redirect
from django.contrib import messages
from models import Actor, Movie

def index(request):
    return render(request, 'buff/index.html')

def add_actor(request):

    context = {
        'actors':Actor.objects.all()[::-1]
    }
    return render(request, 'buff/index.html', context)

def add_movie(request):
    context = {
        'movies':Movie.objects.all()[::-1]
    }
    return render(request, 'buff/index.html', context)
