from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/class_rooms/', views.class_rooms, name='class_rooms'),
    path('home/class_rooms/class_detail/<int:id>/', views.class_detail, name='class_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)