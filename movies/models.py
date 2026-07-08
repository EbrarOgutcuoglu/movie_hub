from django.db import models
from directors.models import Director

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    description = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100) # Ready for future grouping/filtering
    rating = models.FloatField(default=0.0) # Store ratings out of 5.0 (e.g. 4.8)
    poster_url = models.URLField(blank=True, null=True, default="https://via.placeholder.com/300x450")
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title