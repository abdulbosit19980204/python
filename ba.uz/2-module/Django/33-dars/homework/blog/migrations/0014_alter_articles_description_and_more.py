# Generated by Django 5.0.2 on 2024-02-28 20:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_comments_article_id_articles_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_message',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
