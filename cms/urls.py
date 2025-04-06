from django.contrib import admin
from django.urls import path
from content import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
]