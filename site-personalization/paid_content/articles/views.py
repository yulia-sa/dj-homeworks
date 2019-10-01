from django.shortcuts import render, get_object_or_404

from .models import Profile, Article


def show_articles(request):
    articles = Article.objects.all()

    if 'is_subscribed' not in request.session.keys():
        request.session['is_subscribed'] = False

    context = {
        'articles': articles,
        'is_subscribed': request.session['is_subscribed']
    }

    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    article = get_object_or_404(Article, id=id)

    if 'is_subscribed' not in request.session.keys():
        request.session['is_subscribed'] = False

    context = {
        'article': article,
        'is_subscribed': request.session['is_subscribed']
    }

    return render(
        request,
        'article.html',
        context
    )


def subscribe(request):
    if 'is_subscribed' not in request.session.keys():
        request.session['is_subscribed'] = False

    action = request.GET.get('action')

    if action == 'subscribe':
        request.session['is_subscribed'] = True
    elif action == 'unsubscribe':
        request.session['is_subscribed'] = False
    else:
        pass

    context = {
        'is_subscribed': request.session['is_subscribed']
    }

    return render(
        request,
        'subscription.html',
        context
    )
