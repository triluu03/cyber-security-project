# Generated by Django 4.1.3 on 2023-11-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_alter_book_suggested_by_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
            ],
        ),
    ]
