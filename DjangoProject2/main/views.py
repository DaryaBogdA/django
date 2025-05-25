from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView
def index(request):
    news = Article.objects.order_by('-date')
    return render(request, 'main/index.html', {'news' : news})

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')

class NewsDetailView(DetailView):
    model = Article
    template_name = 'main/details_view.html'
    context_object_name = 'article'
