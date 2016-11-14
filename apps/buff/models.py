from __future__ import unicode_literals
from django.db import models

class ActorManager(models.Manager):
    def add_actor():
        actor = self.create(actor_name=request.POST['actor_name'])
    def update_actor():
        pass

class MovieManager(models.Manager):
    def add_movie():
        movie = self.create(movie_name=request.POST['movie_name'])

class Movie(models.Model):
    movie_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MovieManager()

class Actor(models.Model):
    actor_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    actor_movies = models.ManyToManyField(Movie)

    objects = ActorManager()
