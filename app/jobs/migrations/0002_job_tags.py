# Generated by Django 4.1.1 on 2022-09-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="tags",
            field=models.ManyToManyField(to="jobs.tag"),
        ),
    ]
