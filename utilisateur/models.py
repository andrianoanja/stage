from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
    
class Utilisateur(AbstractUser):
    telephone=models.CharField(max_length=15)
    profile=models.ImageField(upload_to="utilisateur")
    
    def __str__(self):
        return self.username