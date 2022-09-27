from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Provider


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):
            Provider.objects.get_or_create(
                title=fake.prefix_nonbinary(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                middle_initial=fake.last_name()[:1]
            )