# Generated by Django 4.1.2 on 2022-10-24 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0010_alter_vaccination_b_date_alter_vaccination_i_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination1",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination2",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination3",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination4",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination5",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination6",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination7",
        ),
        migrations.RemoveField(
            model_name="immunisationstatement",
            name="vaccination8",
        ),
        migrations.RemoveField(
            model_name="vaccination",
            name="b_date",
        ),
        migrations.RemoveField(
            model_name="vaccination",
            name="i_date",
        ),
        migrations.AddField(
            model_name="immunisationstatement",
            name="b_date",
            field=models.DateField(blank=True, null=True, verbose_name="booster due"),
        ),
        migrations.AddField(
            model_name="immunisationstatement",
            name="i_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="injection date"
            ),
        ),
    ]