from django.urls import path
from music import views


urlpatterns = [
    path('home/', views.home, name='homepage'),
    path('contactus/', views.contactus, name='homepage'),
    path('home/albums/', views.albums_list, name='albums_list'),
    path('home/albums/create/', views.AlbumCreate, name='albums_create'),
    path('home/albums/<int:id>/', views.album_detail, name='album_detail'),
    path('media/', views.media_error, name='media_error'),
]
