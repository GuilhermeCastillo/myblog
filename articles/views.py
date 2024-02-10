from django.shortcuts import render
from articles.models import Article


# Create your views here.
def articles_view(request):
    articles = Article.objects.all()
    search = request.GET.get("search")

    if search:
        articles = Article.objects.filter(title__icontains=search)

    return render(request, "articles.html", {"articles": articles})

def new_article_view(request):
    return