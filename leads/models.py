from django.db import models

# Create your models here.
class Lead(models.Model):
    
    name = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=256)
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

class CarearEmployee(models.Model):
    
    name = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    applied_for = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} - {self.applied_for}'
    