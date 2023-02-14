from django.db import models
from django_countries.fields import CountryField


class DeliveryOptionManager(models.Manager):
    pass


class DeliveryOption(models.Model):
    REGION_CHOICES = (
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('US', 'US'),
    )
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    option = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    objects = DeliveryOptionManager()
