from django.contrib import admin
from posts.models import Post, PostRead


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']


admin.site.register(Post, PostAdmin)
admin.site.register(PostRead)