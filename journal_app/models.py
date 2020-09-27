from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 	If True, Django will store empty values as NULL in the database. 
# Default is False.
# Blank	If True, the field is allowed to be blank. Default is False.
# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text_area = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
  