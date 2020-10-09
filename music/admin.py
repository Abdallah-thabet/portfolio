from django.contrib import admin
from .models import Album, Song


# Register your models here.
for model in [Album, Song]:
    admin.site.register(model)
