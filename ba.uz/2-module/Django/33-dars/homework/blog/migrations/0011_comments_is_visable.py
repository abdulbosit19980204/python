# Generated by Django 5.0.2 on 2024-02-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='is_Visable',
            field=models.BooleanField(default=True),
        ),
    ]
