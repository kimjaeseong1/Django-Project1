from distutils.command.upload import upload
from django.db import models
from acc.models import User
from django.utils import timezone
# Create your models here.

class First(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    pic = models.ImageField(upload_to="club/%y/%m" )


    def __str__(self):
        return self.subject

class Club(models.Model):
    first = models.ForeignKey(First,on_delete=models.CASCADE,null=True)
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,related_name="club_user",on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=100,default='')
    content = models.TextField(default='')
    pudate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first}_{self.subject}"

class Image(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    image = models.ImageField(default='media/club/default_image.jpeg', upload_to='club',blank=True,null = True)

    def __str__(self):
        return f"{self.club}_{self.image}"

class Detail(models.Model):
    first = models.ForeignKey(First,on_delete=models.CASCADE,null=True)
    제목 = models.CharField(max_length=100)
    content = models.TextField(default='')
    def __str__(self):
        return self.제목

    
