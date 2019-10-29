from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from books.models import Author

class Command(BaseCommand):
    help = 'Create 10 fake authors'


    def handle(self, *args, **options):
        faker = Faker("pl_PL")
        for i in range(10):
            author = Author()
            author.firstname = faker.first_name()
            author.lastname = faker.last_name()
            author.birtday = faker.date_of_birth()
            author.save()
            self.stdout.write(self.style.SUCCESS(f'Create:{str(author)}'))