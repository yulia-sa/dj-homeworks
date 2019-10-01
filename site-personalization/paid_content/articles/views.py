from django.shortcuts import render, get_object_or_404

from .models import Profile, Article


def create_user(request):
    if not request.session.session_key:
        request.session.save()
    
    if request.session.get('user_id', False):
        user_id = int(request.session['user_id'])

    else:
        new_user = Profile(name=request.session.session_key)
        new_user.save()
        user_id = new_user.id
        request.session['user_id'] = user_id
        
    return user_id


def show_articles(request):
    create_user(request)

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
    create_user(request)

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
    user_id = create_user(request)
    user = Profile.objects.filter(id=user_id)[0]

    if 'is_subscribed' not in request.session.keys():
        request.session['is_subscribed'] = False

    action = request.GET.get('action')

    if action == 'subscribe':
        request.session['is_subscribed'] = True
        user.is_subscribed = True
        user.save()

    elif action == 'unsubscribe':
        request.session['is_subscribed'] = False
        user.is_subscribed = False
        user.save()
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
