from django.contrib import admin

from posts.models import AuthorModel, TagModel, PostModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author', 'tags']