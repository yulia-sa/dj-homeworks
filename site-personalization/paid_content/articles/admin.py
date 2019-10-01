from django.contrib import admin

from .models import Profile, Article


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_subscribed')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_paid')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article, ArticleAdmin)