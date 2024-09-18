from django.urls import path
from .views import video_upload_view

app_name = 'video_upload'

urlpatterns = [
    path('', video_upload_view, name='video_upload'),
]
