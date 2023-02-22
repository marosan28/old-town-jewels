from django.db import models
from django.utils import timezone
from django.conf import settings
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model


class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    image = CloudinaryField('image')

    def __str__(self):
        return f'Profile of {self.user.username}'
    
    def image_tag(self):
        if self.image:
            return CloudinaryImage(self.image).image(transformation=[
                {'width': 400, 'height': 400, 'crop': 'thumb'},
                {'radius': 'max'},
            ])
        return ''

    image_tag.short_description = 'Profile Picture'


