from django.db import models

# Create your models here.


class Admission(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone= models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    amount=models.IntegerField()

    def __str__(self):
        return self.name