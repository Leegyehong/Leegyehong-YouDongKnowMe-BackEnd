from django.db import models

# Create your models here.
class ApiKey(models.Model):
    name = models.CharField('name', max_length=1024, unique=True)
    email = models.EmailField('email', max_length=128, unique=True)
    apikey = models.TextField('api key', blank=True)
    
    def __str__(self):
        return self.name