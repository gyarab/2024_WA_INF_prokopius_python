from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("hero/<int:hero_id>/", views.hero_detail, name="hero_detail"),
    path("category/<int:category_id>/", views.category_detail, name="category_detail"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
]