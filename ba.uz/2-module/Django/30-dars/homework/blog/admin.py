from django.contrib import admin

from .models import Articles, ContactUs

# Register your models here.

admin.site.register(Articles)
admin.site.register(ContactUs)
