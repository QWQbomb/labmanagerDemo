from datetime import timezone

from django.template.backends import django
from django.utils import timezone
from django.db import models
from django.utils import datetime_safe


# Create your models here.

# 用户账号类
class User(models.Model):
    userId = models.AutoField('用户编号', primary_key=True)
    userName = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=16)
    perInfoId = models.ForeignKey(to='PerInfo',
                                  on_delete=models.CASCADE)
    roleId = models.ForeignKey(to='Role',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.userName


# 用户个人信息类
class PerInfo(models.Model):
    perInfoId = models.AutoField('个人信息编号', primary_key=True)
    name = models.CharField('名字', max_length=20)
    address = models.CharField('地址', max_length=50, null=True, blank=True)  # null 默认值为 False， 所以仅在可为True 时写出
    email = models.CharField('电子邮件', max_length=30, null=True, blank=True)
    telephone = models.CharField('手机号码', max_length=11)

    def __str__(self):
        return self.name


# 角色类
class Role(models.Model):
    roleId = models.AutoField('用户组编号', primary_key=True)
    roleNum = models.CharField('用户组', max_length=10)
    roleName = models.CharField('用户组名', max_length=50)
    remark = models.CharField('备注', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.roleName


# 实验设备类
class Equipment(models.Model):
    eqId = models.AutoField('设备编号', primary_key=True)
    eqName = models.CharField('设备名称', max_length=20, unique=True)  # 设备不允许重名，可在名称后加备注或编号区别
    eqState = models.IntegerField('设备状态',
                                  choices=((0, '空闲'), (-1, '维修/保养'), (1, '已借出')), default=0)

    def __str__(self):
        return self.eqName


# 预约信息类
class Reservation(models.Model):
    reId = models.AutoField('预约编号', primary_key=True)
    # reNum = models.CharField(max_length=30)
    rePer = models.ForeignKey(to='PerInfo',
                              on_delete=models.CASCADE, verbose_name="预约人")
    reEquip = models.ForeignKey(Equipment,to_field='eqName',
                                on_delete=models.CASCADE, verbose_name="预约器材")
    startTime = models.DateTimeField(verbose_name="开始时间", default=timezone.now)  # 待修改
    endTime = models.DateTimeField(verbose_name="结束时间", default=timezone.now)  # 待修改
    approvalPer = models.ForeignKey(to='User',
                                    on_delete=models.CASCADE, verbose_name="批准人")
    reState = models.IntegerField('预约状态', choices=((0, '预约中'), (-1, '拒绝'), (1, '批准'), (2, '已结束')), default=0)


# 实验信息类
class ExpData(models.Model):
    expDataId = models.AutoField(primary_key=True)
    expName = models.CharField(max_length=20)
    expContent = models.CharField(max_length=20)

    def __str__(self):
        return self.expName


# 项目信息类
class Project(models.Model):
    pjId = models.AutoField(primary_key=True)
    # pjNum = models.CharField(max_length=20, unique=True)
    pjName = models.CharField('项目名称', max_length=20)
    responPer = models.CharField('项目负责人', max_length=20)
    applyTime = models.DateTimeField(verbose_name="申请时间", default = timezone.now)#待修改 timezone.now 设置为加入时时间且后续可改
    pjState = models.IntegerField('项目状态', choices=((0, '申请中'), (1, '申请通过'), (2, '中期检查'),
                                                   (3, '结题'), (-1, '申请未通过')), default=0)
    checkTime = models.DateTimeField(verbose_name="审批时间", null=True, blank=True)#待修改
    checkPer = models.CharField('项目检查员', max_length=20)
    remark = models.CharField('备注', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.pjName
