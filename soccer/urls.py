from django.urls import path
from . import views

app_name="soccer"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<spk>',views.detail,name="detail")

]