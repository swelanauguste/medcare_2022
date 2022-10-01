import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Address, District, Provider


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            Address.objects.get_or_create(
                provider=Provider.objects.get(pk=random.randint(1, 20)),
                address1=fake.street_address(),
                address2=fake.street_name(),
                district=District.objects.get(pk=random.randint(1, 12)),
                postal_code=fake.postcode(),
            )
