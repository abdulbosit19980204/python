from django.db import models


# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    view_count = models.IntegerField(default=0)
    creator = models.CharField(max_length=120)
    creator_title = models.CharField(max_length=120)
    creator_image = models.ImageField(upload_to='users/image/')
    article_title_image = models.ImageField(upload_to='posts/image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_page = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    fullName = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    is_responsed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName
