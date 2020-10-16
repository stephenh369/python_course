from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/new/', views.album_new, name='album_new')
]