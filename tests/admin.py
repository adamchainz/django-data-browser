from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin
from django.db.models import F

from . import models

# admin for perm testing


class InlineAdminInline(admin.TabularInline):
    model = models.InlineAdmin
    fields = ["name"]


class GenericInlineAdminInline(GenericInlineModelAdmin):
    model = models.GenericInlineAdmin


@admin.register(models.InAdmin)
class InAdmin(admin.ModelAdmin):
    fields = ["name"]
    inlines = [InlineAdminInline, GenericInlineAdminInline]


@admin.register(models.Normal)
class Normal(admin.ModelAdmin):
    fields = ["name", "in_admin", "not_in_admin", "inline_admin"]


# general admin


@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    fields = ["name"]


@admin.register(models.Address)
class Address(admin.ModelAdmin):
    fields = ["pk", "city", "bob", "fred", "tom"]
    readonly_fields = ["bob", "fred", "tom"]

    def bob(self, obj):
        assert obj.street != "bad", obj.street
        return "bob"


class ProductMixin:
    fields = [
        "id",
        "producer",
        "name",
        "size",
        "size_unit",
        "producer",
        "is_onsale",
        "default_sku",
        "tags",
        "model_not_in_admin",
        "onsale",
        "image",
        "created_time",
        "annotated",
        "derived",
    ]
    readonly_fields = ["is_onsale", "annotated", "derived"]

    def derived(self, obj):
        return f"D{obj.name}"

    derived.admin_order_field = "name"

    def annotated(self, obj):
        return f"A{obj.annotated_qs}"

    annotated.admin_order_field = "annotated_qs"

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(annotated_qs=F("name"))


class ProductInline(ProductMixin, admin.TabularInline):
    model = models.Product


@admin.register(models.Producer)
class Producer(admin.ModelAdmin):
    fields = ["name", "address", "frank"]
    readonly_fields = ["frank"]
    inlines = [ProductInline]

    def frank(self, obj):
        return "frank"


class SKUInline(admin.TabularInline):
    model = models.SKU
    fields = ["name", "product", "bob"]
    readonly_fields = ["bob"]

    def bob(self, obj):  # pragma: no cover don't show funcs on inlines test
        return "bob"


@admin.register(models.Product)
class Product(ProductMixin, admin.ModelAdmin):
    inlines = [SKUInline]
    list_display = ["only_in_list_view"]
