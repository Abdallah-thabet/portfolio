from django.contrib import admin
from .models import Classroom, Teacher, Student 


# Register your models here.
for model in [Classroom, Teacher, Student]:
    admin.site.register(model)
