from django.core.management.base import BaseCommand


from ...models import Tag



class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        # file_name = kwargs["file_name"]
        with open(f"tag_list.txt") as file:
            for row in file:
                tag = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{tag} added"))
                Tag.objects.get_or_create(tag=tag,)
        self.stdout.write(self.style.SUCCESS("list of tags added"))