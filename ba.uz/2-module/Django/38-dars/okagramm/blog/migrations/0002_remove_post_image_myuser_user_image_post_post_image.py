# Generated by Django 5.0.3 on 2024-03-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='media/'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='media/'),
        ),
    ]
