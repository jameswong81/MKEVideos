from django.shortcuts import render, redirect
import requests
from django.conf import settings
from isodate import parse_duration

# Create your views here.
def test_view(request):
    return render(request, template_name='Home/test.html')


def upload_file(request):
    if request.method == 'POST':
        pass
    else: # get
        return render(request, template_name='Home/upload.html')

#Coded Homepage
def videos(request):
    videos = []

    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part': 'snippet',
        'q': 'Milwaukee',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 50,
        'type': 'video'
    }

    r = requests.get(search_url, params=search_params)

    results = r.json()['items']

    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])


    video_params = {
        'key': settings.YOUTUBE_DATA_API_KEY,
        'part': 'snippet,contentDetails',
        'id': ','.join(video_ids),
        'maxResults': 50
    }

    r = requests.get(video_url, params=video_params)

    results = r.json()['items']

    for result in results:
        video_data = {
            'title': result['snippet']['title'],
            'id': result['id'],
            'url': f'https://www.youtube.com/watch?v={result["id"]}',
            'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail': result['snippet']['thumbnails']['high']['url']
        }

        if video_data["duration"] <= 5:
            videos.append(video_data)

    context = {
        'videos': videos
    }

    return render(request, "Home/videos.html", context)

