from django.contrib import admin

from .models import Articles, ContactUs


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'is_responsed', 'created_at')
    list_display_links = ('id', 'fullName', 'is_responsed')


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'main_page', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'creator')


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(ContactUs, ContactAdmin)
