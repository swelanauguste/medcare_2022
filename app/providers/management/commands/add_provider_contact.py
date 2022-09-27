import random

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Contact, Provider


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        # print(fake.simple_profile()['mail'])
        for _ in range(100):
            Contact.objects.get_or_create(
                provider=Provider.objects.get(pk=random.randint(1, 100)),
                tel1=fake.msisdn(),
                tel2=fake.msisdn(),
                email=fake.simple_profile()['mail']
            )
