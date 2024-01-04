from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    image = models.ImageField(upload_to='media', null=True, blank=True)