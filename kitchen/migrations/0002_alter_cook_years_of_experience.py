# Generated by Django 4.2.1 on 2023-06-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
