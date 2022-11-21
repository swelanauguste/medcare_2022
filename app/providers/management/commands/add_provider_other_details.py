import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import OtherDetail, Provider


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):
            OtherDetail.objects.get_or_create(
                provider=Provider.objects.get(pk=random.randint(1, 20)),
                driver_license=random.randint(0, 1),
            )
