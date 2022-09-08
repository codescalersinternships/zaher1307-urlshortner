from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shorten_link/', views.shorten_link, name='shorten_link'),
]