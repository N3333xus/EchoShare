from django.contrib import admin

# Register your models here.

from echoshare_blog.models import Post, Category, About

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(About)