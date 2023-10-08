from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Video(Content):
    video_file = models.FileField(upload_to='videos/')

class Document(Content):
    pdf_file = models.FileField(upload_to='pdfs/')

