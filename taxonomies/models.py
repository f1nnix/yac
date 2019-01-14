from django.db import models
from main.models import AbstractBase


# Create your models here.
class Tag(AbstractBase):
    slug = models.SlugField(max_length=128, blank=False, null=False)
    title = models.TextField(max_length=512, blank=False, null=False)
