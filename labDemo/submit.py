# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求数据
from pymysql.constants.FIELD_TYPE import CHAR


def submit_post(request):
    # ctx = {}
    errors = []
    if request.POST:
        if not request.POST.get('user_name', ''):
            errors.append('Enter a user_name.')
        if not request.POST.get('password', ''):
            errors.append('Enter a password.')
        if not request.POST.get('name', ''):
            errors.append('Enter a name.')
        if not request.POST.get('email', ''):
            errors.append('Enter a email.')
        # ctx['rlt'] = request.POST['user_name']
        # send_mail('Subject here', 'Here is the message.', 'ybw.x@qq.com',
        #  ['ybw.x@qq.com'], fail_silently=False)
        if not errors:
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            name = request.POST.get('name')
            email = request.POST.get('email')
            send_mail(
                '测试邮件',
                '新用户申请注册' + '\n'
                + '用户名：' + user_name + '\n'
                + '密码：' + password + '\n'
                + '姓名：' + name + '\n'
                + '电子邮箱：' + email + '\n',
                'ybw.x@qq.com',
                ['ybw.x@qq.com'],
                fail_silently=False,
            )
            messages.error(request, "表单已提交")
    return render(request, "registForm.html")
