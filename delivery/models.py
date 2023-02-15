from django.db import models

class DeliveryOption(models.Model):
    name = models.CharField(max_length=50, default='Standard Shipping')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=5.99)

    def __str__(self):
        return self.name

