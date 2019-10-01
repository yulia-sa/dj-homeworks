"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from articles.views import show_articles, show_article, subscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_articles),
    path('subscription/', subscribe, name='subscription'),
    path('articles/', show_articles),
    url(r'^articles/(?P<id>[0-9]+)/', show_article, name='show_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
