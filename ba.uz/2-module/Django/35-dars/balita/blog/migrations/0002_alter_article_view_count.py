# Generated by Django 5.0.2 on 2024-03-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
