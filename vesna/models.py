from django.db import models

# Create your models here.

class AppFile(models.Model):
    file = models.FileField()
