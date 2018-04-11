from django.db import models
from uuid import uuid4

# Create your models here.


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    notes = models.TextField('Notes', blank=True)
    url = models.URLField('URL', unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
