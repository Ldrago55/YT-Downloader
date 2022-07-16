from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('youtube', views.youtube, name='youtube'),
    path('search', views.search, name='search'),
]