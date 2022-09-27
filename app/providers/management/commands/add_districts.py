import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import District

DISTRICTS = [
    "gros islet",
    "castries",
    "anse la raye",
    "caneries",
    "soufriere",
    "choisuel",
    "laborie",
    "vieux fort",
    "micoud",
    "parlsin",
    "dennery",
    "dophin",
]


class Provider(faker.providers.BaseProvider):
    def districts(self):
        return self.random_element(DISTRICTS)


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        fake.add_provider(Provider)

        for _ in range(12):
            District.objects.get_or_create(district_name=fake.districts())