from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pic = models.ImageField(upload_to="user/%y/%m")
    age = models.IntegerField(null=True)
    comment = models.TextField()
    birth_date = models.DateTimeField(null=True, blank=True)


    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"