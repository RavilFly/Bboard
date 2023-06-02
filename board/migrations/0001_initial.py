# Generated by Django 4.2.1 on 2023-06-02 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "cat",
                    models.CharField(
                        choices=[
                            ("Tanks", "Танки"),
                            ("Heales", "Хилы"),
                            ("DD", "ДД"),
                            ("Traders", "Торговцы"),
                            ("Guildmasters", "Гилдмастеры"),
                            ("Questgivers", "Квестгиверы"),
                            ("Blacksmiths", "Кузнецы"),
                            ("Tanners", "Кожевники"),
                            ("Poitionsmasters", "Зельевары"),
                            ("Spellmasters", "Мастера заклинаний"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("content", models.TextField()),
                ("time_in", models.DateTimeField(auto_now_add=True)),
                ("file", models.FileField(upload_to="user_media")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="board.category"
                    ),
                ),
            ],
        ),
    ]
