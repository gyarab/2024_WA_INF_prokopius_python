from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('genre/<int:genre_id>/', views.genre, name='genre'),
]
