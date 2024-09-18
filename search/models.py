from django.db import models
from video_upload.models import Video  # Import Video from video_upload

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='search_subtitles')  # Correct the reference to Video
    start_time = models.FloatField()  # Start time in seconds
    end_time = models.FloatField()  # End time in seconds
    text = models.TextField()

    def __str__(self):
        return f"{self.start_time}: {self.text}"
