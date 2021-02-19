from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def equ_list(request):
    equ_list = models.Equipment.objects.all()
    return render(request, "equ_list.html",
                  {"equ_list": equ_list})


def add_equ(request):
    if request.method == "POST":
        # 1. 获取表单提交的内容
        equ_name = request.POST.get("equ_name")
        equ_state = request.POST.get("equ_state")
        # 2. 保存到数据库
        models.Equipment.objects.create(eqName=equ_name ,eqState=equ_state)
        # 3. 实现提交完成后页面跳转
        return redirect("/labDemo/equ_list")
    return render(request, "add_equ.html")
