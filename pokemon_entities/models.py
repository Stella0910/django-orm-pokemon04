from django.db import models  # noqa F401

from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
