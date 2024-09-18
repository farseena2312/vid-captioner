from django.db import models
from video_upload.models import Video

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_processing_subtitles')
    language = models.CharField(max_length=50)
    subtitle_file = models.FileField(upload_to='subtitles/')


    def __str__(self):
        return f"Subtitles for {self.video.title} in {self.language}"