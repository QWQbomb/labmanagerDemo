from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("equ_list", views.equ_list),
    path("add_equ", views.add_equ),
]