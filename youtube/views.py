from django.shortcuts import render
from pytube import *
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        messages.info(request, 'Video Downloaded........')
        return render(request, 'index.html', {'url': url})
    return render(request, 'index.html')







