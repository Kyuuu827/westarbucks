from django.urls import path

from movies.views import GetActor, GetMovie

urlpatterns = [
    path('getactor', GetActor.as_view()),
    path('getmovie', GetMovie.as_view()),
]