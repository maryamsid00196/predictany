from django.db import models

class YouTubeVideo(models.Model):
    video_id = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    video_link = models.URLField()
    channel_title = models.CharField(max_length=200)
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title
