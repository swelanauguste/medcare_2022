from django.core.management.base import BaseCommand


from providers.models import District



class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        # file_name = kwargs["file_name"]
        with open(f"district_list.txt") as file:
            for row in file:
                district_name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{district_name} added"))
                District.objects.get_or_create(district_name=district_name,)
        self.stdout.write(self.style.SUCCESS("list of districts added"))