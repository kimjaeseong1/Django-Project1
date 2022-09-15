from django.urls import path
from . import views

app_name="praise"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<ppk>', views.detail,name="detail"),
    path('update/<ppk>',views.update,name="update"),
    path('create/',views.create,name="create"),
    path('delete/<ppk>',views.delete,name="delete")

]