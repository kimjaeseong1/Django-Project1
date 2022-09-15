from django.urls import path
from . import views

app_name="club"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<cpk>',views.detail, name="detail"),
    path('detail2/<cpk>',views.detail2,name="detail2"),
    path('create/',views.create,name="create")
]