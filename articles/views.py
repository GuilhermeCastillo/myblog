from django.shortcuts import render
from articles.models import Article


# Create your views here.
def articles_view(request):
    articles = Article.objects.all()
      
    return render(request, "articles.html", {"articles": articles})
