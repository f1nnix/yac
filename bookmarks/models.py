from django.db import models
from main.models import AbstractBase
from taxonomies.models import Tag


# Create your models here.
class Bookmark(AbstractBase):
    url = models.URLField(null=False, blank=False)
    title = models.TextField(max_length=1024, blank=True, null=True)
    description = models.TextField(max_length=4096, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.url if self.title is None else self.url
