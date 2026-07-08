# directors/models.py
from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, default="https://via.placeholder.com/150")

    def __str__(self):
        return self.name