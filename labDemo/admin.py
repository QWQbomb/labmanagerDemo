from django.contrib import admin

# Register your models here.
from .models import User, PerInfo, Role, Equipment, Reservation, ExpData, Project

admin.site.site_header = '实验室管理系统'


# admin.site.register(User)

@admin.register(PerInfo)
class PerInfo(admin.ModelAdmin):
    # 多用户隔离试行代码
    # def get_queryset(self, request):
    #     qs = super(PerInfo, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)
    list_display = ('name', 'address', 'email', 'telephone')
    list_display_links = ('name',)
    list_per_page = 10
    # list_editable = ('address', 'email', 'telephone')


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ('reId', 'rePer', 'approvalPer', 'reState', 'startTime', 'endTime', 'reEquip')
    list_display_links = ('reId', )
    list_filter = ('reState',)
    list_per_page = 10
    list_editable = ('reState',)


# 暂时不需要重写
admin.site.register(ExpData)


# admin.site.register(Role)
@admin.register(Equipment)
class Equipment(admin.ModelAdmin):
    list_display = ('eqId', 'eqName', 'eqState')
    list_display_links = ('eqName',)
    list_filter = ('eqState',)
    list_per_page = 10
    list_editable = ('eqState',)
    search_fields = ('eqName',)

    def has_add_permission(self, request):
        # 可在此处禁用添加按钮
        user_per_set = request.user.get_all_permissions()  # 获取当前用户权限
        # 待判断的权限范围
        curr_per_set = {'labDemo.view_equipment', 'labDemo.delete_equipment', 'labDemo.add_equipment'}
        if 'labDemo.add_equipment' in curr_per_set.intersection(user_per_set):
            return True
        else:
            return False

        # 可在此处禁用删除按钮
    def has_delete_permission(self, request, obj=None):
        user_per_set = request.user.get_all_permissions()  # 获取当前用户权限
        # 待判断的权限范围
        curr_per_set = {'labDemo.view_equipment', 'labDemo.delete_equipment', 'labDemo.add_equipment'}
        if 'labDemo.delete_equipment' in curr_per_set.intersection(user_per_set):
            return True
        else:
            return False


@admin.register(Project)
class Project(admin.ModelAdmin):
    # 设置页面可以展示的字段
    list_display = ('pjName', 'responPer', 'pjState', 'checkPer', 'remark', 'applyTime', 'checkTime')
    # 默认不配置的话，第一个字段会存在链接到记录编辑页面
    # list_display_links = None
    list_display_links = ('pjName',)
    # 设置过滤选项
    list_filter = ('responPer', 'checkPer',)
    # 每页显示条目数 缺省值100
    list_per_page = 10
    # show all页面上的model数目，缺省200
    # list_max_show_all = 200
    # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
    list_editable = ('remark', 'pjState')
    # 按日期月份筛选 该属性一般不用
    # date_hierarchy = 'CREATED_TIME'
    # 按发布日期降序排序
    # ordering = ('-CREATED_TIME',)
    # 搜索条件设置
    search_fields = ('pjName',)
    # 表头字段显示中文名称，这里需要修改models文件，在定义字段的时候增加别名
    # eg1：JOB_NAME = models.CharField('任务名称',max_length=128)
    # eg2: name = models.CharField(max_length=30,verbose_name="姓名")

    """
      这种禁用编辑链接的放法只是不让它在页面中显示，即把超链接去掉了，
      但是还是可以通过手动输入url的方式来进入编辑页面。
      不过可以配合设置fieldsets或者readonly_fieldss来达到目的
      注意：这里建议删除按钮要禁用掉，否则只有拥有view权限的人员依然可以进行删除动作，或者需要进行人员角色判断
    """

    # def has_add_permission(self, request):
    #     # 可在此处禁用添加按钮
    #     def has_add_permission(self, request):
    #         # user_per_set = request.user.get_all_permissions()  # 获取当前用户权限
    #         # # 待判断的权限范围
    #         # curr_per_set = {'labDemo.view_Project', 'labDemo.delete_Project', 'labDemo.add_Project',
    #         #                 'labDemo.change_Project'}
    #         # if 'labDemo.add_Project' in curr_per_set.intersection(user_per_set):
    #         #     return True
    #         # else:
    #         #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     # 可在此处禁用删除按钮
    #     def has_delete_permission(self, request):
    #         # user_per_set = request.user.get_all_permissions()  # 获取当前用户权限
    #         # # 待判断的权限范围
    #         # curr_per_set = {'labDemo.view_Project', 'labDemo.delete_Project', 'labDemo.add_Project',
    #         #                 'labDemo.change_Project'}
    #         # if 'labDemo.delete_Project' in curr_per_set.intersection(user_per_set):
    #         #     return True
    #         # else:
    #         #     return False
