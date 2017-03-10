from django.db import models

# Create your models here.

class Scientist(models.Model):
    women_number = models.IntegerField(default=0)
    men_number = models.IntegerField(default=0)
    specialization = models.CharField(max_length=128)
