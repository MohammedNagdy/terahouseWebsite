from django.db import models

# Create your models here.

# a model that takes the order from the user
class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    storage = models.IntegerField(default=1)
    bandwidth = models.IntegerField(default=1)
    email_accounts = models.IntegerField(default=1)
    price = models.IntegerField()
