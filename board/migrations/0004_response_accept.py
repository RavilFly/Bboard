# Generated by Django 4.2.1 on 2023-06-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0003_alter_post_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="response",
            name="accept",
            field=models.CharField(max_length=1, null=True),
        ),
    ]
