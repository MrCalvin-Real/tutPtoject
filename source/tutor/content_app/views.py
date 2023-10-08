# Create your views here.
from .models import Video
from .forms import VideoForm

# @login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required  # Require authentication to access this view
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.save()
            return redirect('home')
    else:
        form = VideoForm()

    return render(request, 'content_app/video_create.html', {'form': form})


def edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_detail', video_id=video_id)  # Redirect to video detail page
    else:
        form = VideoForm(instance=video)

    return render(request, 'content_app/edit_video.html', {'form': form, 'video': video})


def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'content_app/video_detail.html', {'video': video})


@login_required
def home(request):


    video = Video.objects.first()  # Replace with your video retrieval logic

    context = {
        'user': request.user,
        'video': video,'year': 2023  # Include the video object in the context
    }

    return render(request, 'home.html', context)
