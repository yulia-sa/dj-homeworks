from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().prefetch_related('articlescope_set').order_by('-published_at')
    context = {
        'object_list': object_list
    }

    return render(request, template, context)
