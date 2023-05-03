import uuid
from django.db import models
from slugify import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)
