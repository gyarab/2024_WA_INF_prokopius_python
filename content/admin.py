from django.contrib import admin
from content.models import Book
from content.models import Author
from content.models import Genre

# Register your models here.

admin.site.register([
    Book,
    Author,
    Genre
])