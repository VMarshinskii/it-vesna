from django.contrib.auth.models import User
from django.db import models

class Application(models.Model):

    author = models.ForeignKey(User)

    title = models.CharField(max_length=5000)

class AppFile(models.Model):
    file = models.FileField()
