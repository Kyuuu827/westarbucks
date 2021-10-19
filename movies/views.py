from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views import View
from movies.models import Actor, Movie


class GetActor(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []       
        for actor in actors:
            title_list = []
            for movie in actor.movies.all():
                title_list.append(movie.title)
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
        results = []
        for movie in movies:
            actor_list = []
            for actor in movie.actor.all():
                actor_list.append(actor.last_name)
            results.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "actor" : actor_list
                }
            )        
        return JsonResponse({"RESULTS" : results}, status = 200)
