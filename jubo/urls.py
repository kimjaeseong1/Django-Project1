from django.urls import path
from . import views


app_name="jubo"
urlpatterns = [
    path('index/',views.index,name="index")
]