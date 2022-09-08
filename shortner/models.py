from pyexpat import model
from django.db import models

class URL(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)