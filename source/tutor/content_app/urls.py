from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_video/', views.video_create, name='video_create'),
    path('edit_video/<int:video_id>/', views.edit_video, name='edit_video'),
    path('video_detail/<int:video_id>/', views.video_detail, name='video_detail'),
]
