from django.db import models
from django.utils import timezone

# Album model
class Album(models.Model):
    title = models.CharField(max_length=255, default = '')
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    date = models.DateField(null=True, blank=True)
    songcount = models.PositiveIntegerField(null=True, blank=True)
