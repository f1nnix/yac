from django.db import models
from django.contrib.postgres.fields import JSONField


class AbstractBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta = JSONField(default=dict)

    class Meta:
        abstract = True
