from django.db import models
from django.utils import timezone
from django.conf import settings
import cloudinary


class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

    def image_url(self):
        if self.photo:
            return cloudinary.utils.cloudinary_url(self.photo_public_id)[0]
        return ""