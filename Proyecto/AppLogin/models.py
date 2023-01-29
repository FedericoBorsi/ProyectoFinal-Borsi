from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    imagen = models.ImageField(upload_to = "Avatars")
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

class Descripcion(models.Model):
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

class Link(models.Model):
    url = models.URLField()
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)