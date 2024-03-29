# Generated by Django 4.1.2 on 2022-10-24 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0005_worktype_workinterest"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shift",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="WorkSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="workinterest",
            name="other_commitments",
            field=models.BooleanField(
                default=False, verbose_name="Do you have other commitments?"
            ),
        ),
        migrations.AddField(
            model_name="workinterest",
            name="preferred_shift",
            field=models.ManyToManyField(to="providers.shift"),
        ),
        migrations.AddField(
            model_name="workinterest",
            name="work_schedule",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="providers.workschedule",
            ),
        ),
    ]
