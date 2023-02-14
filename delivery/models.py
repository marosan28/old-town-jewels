from django.db import models

class DeliveryOption(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

