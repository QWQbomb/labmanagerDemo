from django.conf.urls import url
from django.urls import path
from . import views,submit
import notifications.urls

urlpatterns = [
    path("", views.registForm),
    path("equ_list", views.equ_list),
    path("add_equ", views.add_equ),
    path("registForm", views.registForm),
    url(r'^regist/$',views.registForm),
    url(r'^submit/$', submit.submit_post),
]
