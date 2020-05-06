from django.db import models

# Create your models here.
class Stu(models.Model):
    name=models.CharField(default='dqd',max_length=16)