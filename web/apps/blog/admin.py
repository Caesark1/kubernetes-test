from django.contrib import admin

from .models import Tag, Blog


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'likes')
