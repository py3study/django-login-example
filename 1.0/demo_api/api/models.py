from django.db import models

# Create your models here.
class User(models.Model):   #用户名表
    username = models.CharField(max_length=16,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    position = models.CharField(max_length=16,verbose_name="职位")
    email = models.EmailField(max_length=32,verbose_name="邮箱")
    role = models.BooleanField(verbose_name="角色：1.管理员 2.普通用户")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    last_time = models.DateTimeField(verbose_name="登录时间")