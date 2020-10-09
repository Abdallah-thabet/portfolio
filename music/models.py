from django.db import models


# Create your models here.
def store_image(instance, filename):
    return './'.join(['music/images', filename])


def mp3(instance, filename):
    return './'.join(['music/musics', filename])


class Album(models.Model):
    singer = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    logo = models.ImageField(blank=True, null=True, upload_to=store_image) #! it can be FileFiled 

    def __str__(self):
        return f'{self.singer} --- {self.title}'


class Song(models.Model):
    title = models.CharField(max_length=40)
    file_type = models.CharField(max_length=20) # Just for View the file type
    file = models.FileField(blank=True, null=True, upload_to=mp3)
    description = models.TextField(default="description for the song", max_length=500)
    album = models.ForeignKey(Album, on_delete=models.CASCADE) #* the album that the song belongs to

    def __str__(self):
        return self.title
