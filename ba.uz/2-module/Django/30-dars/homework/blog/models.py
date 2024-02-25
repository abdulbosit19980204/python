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

    def __str__(self):
        return self.title
