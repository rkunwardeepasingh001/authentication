from django.db import models
from django.contrib.auth.models import AbstractUser

class Auth1(AbstractUser):
  email=models.EmailField(unique=True)
  final_otp=models.IntegerField(null=True)

  def save(self,*args,**kwargs):
    if not self.username:
      self.username=self.email
    super().save(*args,**kwargs)
  def __str__(self):
    return self.email

# Create your models here.
