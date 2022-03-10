from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
