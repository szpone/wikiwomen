from django.db import models

# Create your models here.

class Scientist(models.Model):
    women_number = models.IntegerField
    men_number = models.IntegerField
    specialization = models.CharField(max_length=128)
