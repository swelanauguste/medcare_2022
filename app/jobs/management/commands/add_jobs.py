import random

from django.core.management.base import BaseCommand
from faker import Faker
from providers.models import District, Provider

from ...models import Job, SkillLevel


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            Job.objects.get_or_create(
                name=fake.company(),
                description=fake.paragraph(nb_sentences=7),
                posted_by=Provider.objects.get(pk=random.randint(1, 20)),
                skill_level = SkillLevel.objects.get(pk=random.randint(1,4)),
                hourly_rate=random.randint(7, 15),
                location=District.objects.get(pk=random.randint(1, 12)),
            )
