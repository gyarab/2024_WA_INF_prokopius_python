from django.shortcuts import render, get_object_or_404
from content.models import Book
from content.models import Author
from content.models import Genre

# Create your views here.

def homepage(request):
    return render(request, 'content/homepage.html', {'books' : Book.objects.all()})
    

def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  
    return render(request, 'content/book.html', {'book': book})
def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'content/author.html', {'author': author})
def genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    return render(request, 'content/genre.html', {'genre': genre})