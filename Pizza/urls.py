from django.urls import path
from Pizza import views

urlpatterns = [
    path('', views.index, name="index"),
]
