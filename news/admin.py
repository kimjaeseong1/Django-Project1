from django.contrib import admin
from news.models import Diary, DiaryImage, source
# Register your models here.
admin.site.register(source)
admin.site.register(Diary)
admin.site.register(DiaryImage)