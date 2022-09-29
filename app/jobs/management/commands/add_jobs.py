import random

from django.core.management.base import BaseCommand
from faker import Faker
from providers.models import District, Provider

from ...models import Job


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):
            Job.objects.get_or_create(
                name=fake.company(),
                description=fake.paragraph(nb_sentences=3),
                posted_by=Provider.objects.get(pk=random.randint(1, 100)),
                hourly_rate=random.randint(7, 10),
                location=District.objects.get(pk=random.randint(9, 20)),
            )
