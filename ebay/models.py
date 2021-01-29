from django.db import models
from datetime import datetime

# Create your models here.
class Ebay(models.Model):
    url = models.URLField()
    desired_price = models.IntegerField()
    email = models.EmailField()
    date_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email