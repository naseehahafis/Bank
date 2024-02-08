from django.db import models
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district
