# Generated by Django 2.0.13 on 2020-03-31 16:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="View",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(blank=True)),
                ("public", models.BooleanField(default=False)),
                ("app", models.CharField(max_length=16)),
                ("model", models.CharField(max_length=32)),
                ("fields", models.TextField(blank=True)),
                ("query", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]
