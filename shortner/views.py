from django.shortcuts import render, HttpResponse
import pyshorteners

def shorten_link(request):
    url = request.POST.get('url')
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(url)
    return render(request, 'shorten.html', {'shortened_url': shortened_url})