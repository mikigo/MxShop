from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile


# 在 admin 界面添加用户配置项
class UserProfileAdmin(admin.ModelAdmin):
    ...


# 注册
# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserProfile, UserAdmin)
