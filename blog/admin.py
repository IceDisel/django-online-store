from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'preview')
