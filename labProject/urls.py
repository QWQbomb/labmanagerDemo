"""labProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import notifications.urls
from django.views.generic import RedirectView
from labDemo import submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('labDemo/', include("labDemo.urls")),
    path('notifications/', include(notifications.urls, namespace='notifications')),
    path('', RedirectView.as_view(url='/admin/login')),    #     重定义空路径 直接到后台登录页面
    path('registForm.html', RedirectView.as_view(url='/labDemo/registForm')),
    url(r'^submit/$', submit.submit_post),
]
