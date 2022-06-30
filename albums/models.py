from django.db import models

# Album model
class Album(models.Model):
    artist = models.CharField(max_length=255)
# Artist model