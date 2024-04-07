from django.db import models

# Create your models here.
class Subscribers(models.Model):
    Name = models.CharField(max_length=40)
    Email= models.EmailField(max_length=40)
    def __str__(self):
        return self.Name