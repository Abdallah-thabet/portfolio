from django.shortcuts import render
from .models import Classroom, Teacher
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    return render(request, 'system/home.html')


def class_rooms(request):
    classes_list = Classroom.objects.all()
    teacher = Teacher
    return render(request, 'system/class_rooms.html', {'classes_list':classes_list, 'teacher': teacher})


def class_detail(request, id=None):
    classRoom = get_object_or_404(Classroom, id=id)
    teacher = Teacher
    return render(request, 'system/class_detail.html', {'classRoom': classRoom})
