# Generated by Django 4.0 on 2021-12-29 23:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import tests.core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("city", models.TextField()),
                ("street", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="InAdmin",
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
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="InlineAdmin",
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
                ("name", models.TextField()),
                (
                    "in_admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.inadmin"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NotInAdmin",
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
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Producer",
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
                ("name", models.TextField()),
                (
                    "address",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.address",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.TextField()),
                ("size", models.IntegerField(default=0)),
                ("size_unit", models.TextField()),
                ("onsale", models.BooleanField(null=True)),
                ("image", models.FileField(upload_to="")),
                ("fake", tests.core.models.FakeField()),
                (
                    "created_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("only_in_list_view", models.TextField()),
                ("hidden_inline", models.TextField()),
                ("hidden_model", models.TextField()),
                ("extra_inline", models.TextField()),
                ("extra_model", models.TextField()),
                ("boat", models.FloatField(null=True)),
                ("duration", models.DurationField(null=True)),
                ("date", models.DateField(null=True)),
                ("uuid", models.UUIDField(null=True)),
                ("url", models.URLField(null=True)),
                ("_underscore", models.IntegerField(null=True)),
                ("not_in_admin", models.TextField()),
                (
                    "string_choice",
                    models.CharField(
                        choices=[("a", "A"), ("b", tests.core.models.Word("B"))],
                        max_length=8,
                    ),
                ),
                (
                    "number_choice",
                    models.IntegerField(
                        choices=[(1, "A"), (2, tests.core.models.Word("B"))], default=1
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "name",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                )
            ],
        ),
        migrations.CreateModel(
            name="SKU",
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
                ("name", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.product"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="default_sku",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="core.sku",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="fk_not_in_admin",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.inadmin",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="model_not_in_admin",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.notinadmin",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="producer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_set",
                related_query_name="products",
                to="core.producer",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(to="core.Tag"),
        ),
        migrations.CreateModel(
            name="Normal",
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
                ("name", models.TextField()),
                (
                    "in_admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.inadmin"
                    ),
                ),
                (
                    "inline_admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.inlineadmin",
                    ),
                ),
                (
                    "not_in_admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.notinadmin",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ignored",
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
                ("name", models.TextField()),
                (
                    "in_admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.inadmin"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GenericInlineAdmin",
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
                ("name", models.TextField()),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
    ]
