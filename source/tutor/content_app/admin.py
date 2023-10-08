from django.contrib import admin

# Register your models here.
from .models import Video, Document

admin.site.register(Video)
admin.site.register(Document)