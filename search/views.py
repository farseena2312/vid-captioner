from django.shortcuts import render
from .models import Subtitle


def search_subtitles(request):
    query = request.GET.get('query', '').strip()
    subtitles = None
    if query:
        # Perform case-insensitive search for the query in the subtitles
        subtitles = Subtitle.objects.filter(text__icontains=query)

    return render(request, 'search/search_results.html', {'subtitles': subtitles, 'query': query})
