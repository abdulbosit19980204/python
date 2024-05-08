from django.db import models


# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    bank = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    expiration_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
