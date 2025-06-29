from django.db import models
from django.conf import settings
from .models import Product  # assuming Product already exists

class Auction(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('closed', 'Closed')], default='active')

    def __str__(self):
        return f"Auction for {self.product.name}"
