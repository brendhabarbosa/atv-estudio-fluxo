from django.urls import path
from estudio import views

urlpatterns = [
    path('', views.index, name='index'),
]