import ffmpeg
from celery import shared_task
from video_upload.models import Video
from .models import Subtitle
import os

@shared_task
def extract_subtitles(video_id, language='eng'):
    try:
        # Fetch the video instance
        video = Video.objects.get(id=video_id)
        video_path = video.video_file.path

        subtitle_output = f"{os.path.splitext(video_path)[0]}_{language}.srt"

        # Ensure the output directory exists
        output_dir = os.path.dirname(subtitle_output)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Run ffmpeg to extract subtitles
        ffmpeg.input(video_path).output(subtitle_output, **{'c:s': 'mov_text'}).run()

        # Read the generated subtitle file
        with open(subtitle_output, 'r', encoding='utf-8') as subtitle_file:
            subtitle_text = subtitle_file.read()

        # Store the extracted subtitles in PostgreSQL
        Subtitle.objects.create(video=video, language=language, subtitle_text=subtitle_text)

        # Optionally delete the subtitle file after storing in the database
        if os.path.exists(subtitle_output):
            os.remove(subtitle_output)

    except Video.DoesNotExist:
        print(f"Video with ID {video_id} does not exist.")

    except ffmpeg.Error as ffmpeg_err:
        print(f"Error while running ffmpeg: {ffmpeg_err.stderr.decode()}")

    except Exception as e:
        print(f"Error extracting subtitles: {e}")
