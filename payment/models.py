from django.db import models
from django.utils import timezone


class Payment(models.Model):
    method = models.CharField(max_length=100)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'payment'
