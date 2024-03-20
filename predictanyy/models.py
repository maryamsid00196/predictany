from django.db import models

class YouTubeVideo(models.Model):
    video_id = models.CharField(max_length=100,null=True)
    channel_id = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=200,null=True)
    video_link = models.URLField()
    channel_title = models.CharField(max_length=200,null=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
