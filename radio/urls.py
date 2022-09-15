from django.urls import path
from . import views

app_name="radio"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<rpk>', views.detail, name="detail"),
    path('update/<rpk>', views.update, name="update"),
    path('delete/<rpk>', views.delete ,name="delete"),
    path('create',views.create, name="create")
]