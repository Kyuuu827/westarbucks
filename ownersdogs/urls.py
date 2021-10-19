from django.urls import path

from ownersdogs.views import GetDogs, GetOwners, OwnersView, DogsView 

urlpatterns = [
	path('owners', OwnersView.as_view()), 
    path('dogs', DogsView.as_view()),
    path('getowner', GetOwners.as_view()),
    path('getdog', GetDogs.as_view()),
]