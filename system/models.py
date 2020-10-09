from django.db import models


# Create your models here.
def teacher_image(instance, filename):
    return './'.join(['system/teacher_image', filename])


def student_image(instance, filename):
    return './'.join(['system/student_image', filename])


class Classroom(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="No Description", max_length=300)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=32)
    experience = models.IntegerField(default=2)
    description = models.TextField(default="No Description", max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to=teacher_image)
    teacher_class = models.OneToOneField(Classroom, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    grade = models.IntegerField(default=0)
    description = models.TextField(default="No Description", max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to=student_image)
    student_class = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
