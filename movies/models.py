from django.db import models
from directors.models import Director

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    comment = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100)  # Ready for future grouping/filtering
    rating = models.FloatField(default=0.0)
    poster_url = models.URLField(blank=True, null=True, default="https://via.placeholder.com/300x450")
    release_date = models.DateField(blank=True, null=True)
    trailer_url = models.URLField(max_length=500, blank=True, null=True,
                                  help_text="YouTube Embed URL (ex: https://www.youtube.com/embed/...)")

    def save(self, *args, **kwargs):
        if self.trailer_url:
            video_id = None

            # 1. for embed url
            if 'youtube.com/embed/' in self.trailer_url:
                video_id = self.trailer_url.split('youtube.com/embed/')[1]

            # 2. url link
            elif 'youtu.be/' in self.trailer_url:
                video_id = self.trailer_url.split('youtu.be/')[1]

            # 3. normal link
            elif 'watch?v=' in self.trailer_url:
                video_id = self.trailer_url.split('watch?v=')[1]

            # clean extra parameter
            if video_id:
                if '?' in video_id:
                    video_id = video_id.split('?')[0]
                if '&' in video_id:
                    video_id = video_id.split('&')[0]

                # link for watching
                self.trailer_url = f"https://www.youtube.com/watch?v={video_id}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
