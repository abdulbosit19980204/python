from django.contrib import admin
from .models import Article, Category, Comments

# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comments)
