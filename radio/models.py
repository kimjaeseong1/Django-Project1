
from django.db import models
from acc.models import User
from django.utils import timezone
# Create your models here.


class Radio(models.Model):
    제목 = models.CharField(max_length=100)
    글쓴이 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="글쓴이")
    content = models.TextField()
    pudate = models.DateTimeField(default=timezone.now())

    def __str__(self) :
        return self.제목

    def summary(self):
        if len(self.content) > 100:
            return f"{self.content[:100]}"
        return self.content

