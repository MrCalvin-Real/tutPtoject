from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class CustomUser(AbstractUser):
    # Fields for Custom User
    bio = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_student = models.BooleanField(default=True)
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# Here I create user groups for roles
Group.objects.get_or_create(name='Tutor')
Group.objects.get_or_create(name='Student')

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
