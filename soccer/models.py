from distutils.command.upload import upload

from django.db import models
from acc.models import User
# Create your models here.


class Soccer(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    pic = models.ImageField(upload_to="soccer/%y/%m")

    def __str__(self):
        return self.subject

class Diarys(models.Model):
    soccer = models.ForeignKey(Soccer,on_delete=models.CASCADE,null=True)
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,related_name="diarys_user",on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    pudate = models.DateTimeField()

    def __str__(self):
        return f"{self.soccer}_{self.title}"

class DiaryImages(models.Model):
    diarys = models.ForeignKey(Diarys,on_delete=models.CASCADE,null=True)
    image = models.ImageField(default='media/diarys/default_image.jpeg',upload_to='diarys',blank=True,null = True)
    
    def __str__(self):
        return f"{self.diarys}_{self.image}"