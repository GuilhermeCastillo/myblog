from django.shortcuts import render

# Create your views here.
def articles_view(request):
    return render(request, "articles.html")