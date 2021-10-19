from django.shortcuts import render

import json
from django.http     import JsonResponse
from django.views    import View
from movies.models import Actor, Movie, Actor_movie

# Create your views here.
class GetActor(View):
    def get(self, request):
        actors = Actor.objects.all()
        actorsmovies = Actor_movie.objects.all()
        results = []
        for actor in actors:
            title_list = []
            for num in actorsmovies.filter(actor_id=actor.id):
                title_list.append(Movie.objects.get(id=num.movie_id).title)
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "title" : title_list
                }
            )
        return JsonResponse({'RESULTS' : results}, status = 200)

class GetMovie(View):
    def get(self, request):
        movies = Movie.objects.all()
        actorsmovies = Actor_movie.objects.all()
        results = []
        for movie in movies:
            actor_list = []
            for num in actorsmovies.filter(movie_id=movie.id):
                actor_list.append(Actor.objects.get(id=num.actor_id).first_name)
            results.append(
                {
                    "title" : movie.title,
                    "last_name" : movie.running_time,
                    "actor" : actor_list
                }
            )
        return JsonResponse({'RESULTS' : results}, status = 200)