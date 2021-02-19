from django.contrib import admin

# Register your models here.
from .models import User, PerInfo, Role, Equipment, Reservation, ExpData, Project

admin.site.site_header = '实验室管理系统'
# admin.site.register(User)
admin.site.register(PerInfo)
# admin.site.register(Role)
admin.site.register(Equipment)
admin.site.register(Reservation)
admin.site.register(ExpData)
admin.site.register(Project)