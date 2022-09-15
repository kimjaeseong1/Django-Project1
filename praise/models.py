from django.db import models
from acc.models import User

# Create your models here.

class Praise(models.Model):
    제목 = models.CharField(max_length=100)
    작성자 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="작성자")
    pic = models.ImageField(upload_to="praise/%y/%m")
    content = models.TextField()

    def __str__(self):
        return self.제목
        