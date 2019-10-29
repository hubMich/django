import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from books.models import Book, Author

class Command(BaseCommand):
    help = 'Create 10 fake books'


    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        for i in range(10):
            book = Book()
            book.title = faker.text(50)
            book.isbn = faker.isbn13()
            book.pages = faker.random_number()
            book.cover_type = "soft"
            book.save()
            people = Author.objects.all()
            book.author.add(random.choice(people))
            book.save()
            self.stdout.write(self.style.SUCCESS(f'Create:{book}'))