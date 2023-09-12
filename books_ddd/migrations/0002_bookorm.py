# Generated by Django 4.2.3 on 2023-09-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books_ddd", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookORM",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("owner_uuid", models.CharField(max_length=255)),
                ("some_other_field", models.IntegerField()),
            ],
        ),
    ]