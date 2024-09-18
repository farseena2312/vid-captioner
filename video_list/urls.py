from django.urls import path
from .views import video_list_view, video_detail_view

app_name = 'video_list'

urlpatterns = [
    path('', video_list_view, name='video_list'),
    path('<int:video_id>/', video_detail_view, name='video_detail'),
]
