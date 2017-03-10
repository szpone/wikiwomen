from django.db import models

# Create your models here.


class Scientists(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=64)
    link = models.CharField(max_length=128)
    extra_info = models.CharField(max_length=128, blank=True)


class Specialization(models.Model):
    name = models.CharField(max_length=128)
    scientist = models.ForeignKey(Scientists, on_delete=models.CASCADE)


