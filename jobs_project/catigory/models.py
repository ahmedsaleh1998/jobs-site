from django.db import models

# Create your models here.
class Catigory(models.Model):
    catigory_name=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.catigory_name