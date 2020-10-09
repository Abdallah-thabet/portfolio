from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/contact/', views.contact_form, name='contact'),
    path('home/resume/', views.resume, name='resume'),
]