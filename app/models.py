from django.db import models

# Create your models here.
class Trade(models.Model):
    type = models.CharField(max_length = 4)
    user_id = models.IntegerField()
    symbol = models.CharField(max_length = 10)
    shares = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.BigIntegerField()