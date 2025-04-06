from .models import Article, Author, Category

def db_index(request):
    articles = Article.objects.all()
    return render(request, 'content/index.html', {'articles': articles})

def db_article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'content/detail.html', {'article': article})

def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'content/author_detail.html', {'author': author})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'content/category_detail.html', {'category': category})
