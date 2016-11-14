from __future__ import unicode_literals
from django.db import models

class ActorManager(models.Manager):
    def add_actor():
        pass
    def update_actor():
        pass

class MovieManager(models.Manager):
    def add_movie():
        pass

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
