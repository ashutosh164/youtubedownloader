from django.shortcuts import render, redirect
from pytube import *
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url == '':
            messages.error(request, 'Please enter a valid URL..')
            return redirect('/')
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        messages.info(request, 'Video Downloading please wait.....')
        stream.download()
        messages.info(request, 'Video Downloaded Successfully ........')
        return render(request, 'index.html', {'url': url})
    return render(request, 'index.html')







