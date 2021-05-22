from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')

admin.site.register(Post, PostAdmin)