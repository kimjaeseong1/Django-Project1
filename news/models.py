from distutils.command.upload import upload
from email import contentmanager
from django.db import models
from acc.models import User

# Create your models here.

class source(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    pudate = models.DateTimeField()
    pic = models.ImageField(upload_to="news/%y/%m")

    def __str__(self):
        return self.subject

class Diary(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User,related_name="diary_user",on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class DiaryImage(models.Model):
    diary = models.ForeignKey(Diary,on_delete=models.CASCADE)
    image = models.ImageField(default='media/diary/default_image.jpeg', upload_to='diary',blank=True,null = True)
    
    def __str__(self):
        return f"{self.diary}_{self.image}"