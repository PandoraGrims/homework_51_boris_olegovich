

# Create your models here.
from django.db import models


class Cat(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=1)
    hunger = models.IntegerField(default=40)

    happiness = models.IntegerField(default=40)
