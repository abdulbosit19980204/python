# Generated by Django 5.0.2 on 2024-04-12 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_favoritepost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoritepost',
            old_name='my_user',
            new_name='user',
        ),
    ]