from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import VideoUploadForm
from video_processing.task import extract_subtitles

def video_upload_view(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            extract_subtitles.delay(video.id)  # Trigger background processing
            return redirect(reverse('video_list:video_list'))
    else:
        form = VideoUploadForm()
    return render(request, 'video_upload/upload.html', {'form': form})
