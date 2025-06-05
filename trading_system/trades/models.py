from django.db import models
from django.utils import timezone

# Create your models here.

class Trade(models.Model):

    SIDE_CHOICES = [('BUY', 'Buy'), ('SELL', 'Sell')]

    ticker = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    quantity = models.PositiveIntegerField()
    side = models.CharField(max_length=4,choices=SIDE_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    





