import threading

from django.conf import settings
from django.db import models
from django.http import QueryDict
from django.urls import reverse
from django.utils import crypto, timezone

from .common import MAKE_PUBLIC_CODENAME

global_data = threading.local()


def get_id():
    return crypto.get_random_string(length=12)


class View(models.Model):
    class Meta:
        permissions = [
            (MAKE_PUBLIC_CODENAME, "Can make a saved view publicly available")
        ]

    id = models.CharField(primary_key=True, max_length=12, default=get_id)
    created_time = models.DateTimeField(default=timezone.now)

    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )

    public = models.BooleanField(default=False)
    public_slug = models.CharField(max_length=12, default=get_id, blank=False)

    model_name = models.CharField(max_length=32, blank=False)
    fields = models.TextField(blank=True)
    query = models.TextField(blank=True)

    def get_query(self):
        from .query import Query

        return Query.from_request(self.model_name, self.fields, QueryDict(self.query))

    def public_link(self):
        if self.public:
            if getattr(settings, "DATA_BROWSER_ALLOW_PUBLIC", False):
                url = reverse(
                    "data_browser:view", kwargs={"pk": self.public_slug, "media": "csv"}
                )
                return global_data.request.build_absolute_uri(url)
            else:
                return "Public URL's are disabled in Django settings."
        else:
            return "N/A"

    def google_sheets_formula(self):
        if self.public:
            if getattr(settings, "DATA_BROWSER_ALLOW_PUBLIC", False):
                url = reverse(
                    "data_browser:view", kwargs={"pk": self.public_slug, "media": "csv"}
                )
                url = global_data.request.build_absolute_uri(url)
                return f'=importdata("{url}")'
            else:
                return "Public URL's are disabled in Django settings."
        else:
            return "N/A"

    def __str__(self):
        return f"{self.model_name} view: {self.name}"
