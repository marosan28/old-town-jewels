from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from django.urls import reverse
from cloudinary import CloudinaryImage
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    alt = models.CharField(max_length=200, default='')

    def __str__(self):
        return f'Profile of {self.user.username}'

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.user.id)])


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile for a new user when the user is created.

    Args:
        sender: The sender of the signal.
        instance: The user instance that was created.
        created: A boolean indicating whether the user was created.

    Returns:
        None.
    """
    if created:
        Profile.objects.create(user=instance)



