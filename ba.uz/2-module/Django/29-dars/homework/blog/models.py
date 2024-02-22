from django.db import models


# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    view_count = models.IntegerField(default=0)
    creator = models.CharField(max_length=120)
    creator_title = models.CharField(max_length=120)
    creator_image = models.CharField(max_length=4000)
    article_title_image = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
