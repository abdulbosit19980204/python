# Generated by Django 5.0.2 on 2024-03-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_articles_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
