from django.urls import path
from .views import search_subtitles

urlpatterns = [
    path('', search_subtitles, name='search_subtitles'),
]
