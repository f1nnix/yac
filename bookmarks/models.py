from django.db import models
from main.models import AbstractBase
from taxonomies.models import Tag


# Create your models here.
class Bookmark(AbstractBase):
    url = models.URLField(null=False, blank=False)
    title = models.TextField(max_length=1024, blank=False, null=False)
    description = models.TextField(max_length=4096, blank=False, null=False)
    tags = models.ManyToManyField(Tag)