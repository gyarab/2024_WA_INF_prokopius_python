import json
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Hero, Category, Author

def load_data():
    with open("heroes/data.json", encoding="utf-8") as f:
        return json.load(f)

def homepage(request):
    heroes = load_data()
    return render(request, "heroes/homepage.html", {"heroes": heroes})

def hero_detail(request, hero_id):
    heroes = load_data()
    hero = next((h for h in heroes if h["id"] == hero_id), None)
    if not hero:
        raise Http404("Hrdina nenalezen.")
    return render(request, "heroes/hero_detail.html", {"hero": hero})

def homepage(request):
    heroes = Hero.objects.all()
    categories = Category.objects.all()
    return render(request, "heroes/homepage.html", {"heroes": heroes, "categories": categories})

def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)
    return render(request, "heroes/hero_detail.html", {"hero": hero})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    heroes = Hero.objects.filter(category=category)
    return render(request, "heroes/category_detail.html", {"category": category, "heroes": heroes})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    heroes = Hero.objects.filter(authors=author)
    return render(request, "heroes/author_detail.html", {"author": author, "heroes": heroes})