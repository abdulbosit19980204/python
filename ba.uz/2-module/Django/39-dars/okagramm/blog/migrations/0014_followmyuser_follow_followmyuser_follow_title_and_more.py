# Generated by Django 5.0.3 on 2024-03-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_disable_btn_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='followmyuser',
            name='follow',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='followmyuser',
            name='follow_title',
            field=models.TextField(default='Follow', max_length=15),
        ),
        migrations.AddField(
            model_name='likepost',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
