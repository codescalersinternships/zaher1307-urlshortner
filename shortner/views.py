from django.shortcuts import render, HttpResponse
import pyshorteners


# Create your views here.

def home(request):
    return render(request, 'home.html')

def short(request, url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.chilpit.short(url)
    return render(request, 'shorten.html', {'shortened_url':shortened_url})


def shorten_link(request):
    return short(request, request.POST['url'])
    

