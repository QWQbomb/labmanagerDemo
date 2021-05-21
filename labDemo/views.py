from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . import models
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def registForm(request):
    errors = []
    if request.method == 'POST':
        message = '表单已提交'
        # title='This is mail title.'
        # testmessage='Hello, This is a message'
        # testsender='ybw.x@qq.com'
        # testmail_list=['ybw.x@qq.com',]
        # send_mail(
        #            subject=title,
        #            message=testmessage,
        #            from_email=testsender,
        #            recipient_list=testmail_list,
        #            fail_silently=False,
        #            connection=None
        #        )
        return HttpResponse(message)
    # if request.method == 'POST':
    #     if not request.POST.get('user_name', ''):
    #         errors.append('Enter a user_name.')
    #     if not request.POST.get('password', ''):
    #         errors.append('Enter a password.')
    #     if not errors:
    #         send_mail(
    #             request.POST['user_name'],
    #             request.POST['password'],
    #             request.POST.get('email', '123456@qq.com'),
    #             ['ybw.x@qq.com'],
    #         )
    #         return HttpResponseRedirect('registForm.html')
    # send_mail('Subject here', '用户名：'+ user_name + '密码：'+ password, 'ybw.x@qq.com',['ybw.x@qq.com'], fail_silently=False)
    return render(request, "registForm.html")


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
        models.Equipment.objects.create(eqName=equ_name, eqState=equ_state)
        # 3. 实现提交完成后页面跳转
        return redirect("/labDemo/equ_list")
    return render(request, "add_equ.html")


# send_mail的参数分别是 邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
# send_mail('Subject here', 'Here is the message.', 'ybw.x@qq.com',
#  ['ybw.x@qq.com'], fail_silently=False)

