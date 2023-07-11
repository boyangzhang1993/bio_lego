from django.db import models

class Component(models.Model):
    label = models.CharField(max_length=200)
    order = models.IntegerField()
