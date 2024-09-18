from django.shortcuts import render, get_object_or_404
from video_upload.models import Video
from video_processing.models import Subtitle

def video_list_view(request):
    videos = Video.objects.all()
    return render(request, 'video_list/video_list.html', {'videos': videos})

def video_detail_view(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    subtitles = Subtitle.objects.filter(video=video)
    return render(request, 'video_list/video_details.html', {
        'video': video,
        'subtitles': subtitles
    })
