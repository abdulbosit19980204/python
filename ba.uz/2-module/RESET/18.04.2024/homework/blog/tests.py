from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from .models import Post, Author, Category


class Command(BaseCommand):
    help = 'Generate fake posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        authors = Author.objects.all()
        categories = Category.objects.all()

        for _ in range(20):  # Change 20 to the desired number of fake posts
            author = fake.random_element(authors)
            category = fake.random_element(categories)
            title = fake.sentence()
            description = fake.paragraph()
            is_published = fake.boolean()
            created_at = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
            updated_at = fake.date_time_this_year(before_now=False, after_now=True, tzinfo=None)

            Post.objects.create(
                author=author,
                category=category,
                title=title,
                description=description,
                is_published=is_published,
                created_at=created_at,
                updated_at=updated_at
            )

        self.stdout.write(self.style.SUCCESS('Fake posts created successfully'))
