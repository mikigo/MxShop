from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    # now不要直接调用这个方法，生成实例的时候才调用。
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 不会生成一张表
        abstract = True


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女"),
)


# 覆盖django自带的user表
class UserProfile(AbstractUser):
    """User表"""
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(max_length=50, verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name="性别", choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    image = models.ImageField(upload_to="head_image/%Y/%m", default="default.jpg", verbose_name="用户头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        return self.username
