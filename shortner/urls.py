from django.urls import path
from . import views

urlpatterns = [
    path('shorten_link/', views.shorten_link, name='shorten_link'),
]