from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField('Genre', related_name='books')
    description = models.TextField()
    published_year = models.IntegerField()

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name