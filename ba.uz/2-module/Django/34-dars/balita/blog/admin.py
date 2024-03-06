from django.contrib import admin
from .models import Article, Category, Comments


# Register your models here.
class CategoryInline(admin.TabularInline):
    model = Article
    extra = 3


class ArticleInline(admin.TabularInline):
    model = Comments
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ('id', "name")
    inlines = (CategoryInline,)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "updated_at", "is_published", "view_count")
    list_display_links = ('id', 'title')
    inlines = (ArticleInline,)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", 'article', "created_at")
    list_display_links = ("id", 'article', "created_at")

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comments)
