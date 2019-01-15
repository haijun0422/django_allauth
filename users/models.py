from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    arg = models.CharField(max_length=128, verbose_name='机构')
    tel = models.CharField(max_length=15, verbose_name='电话')
    mod_date = models.DateTimeField(auto_now=True, verbose_name='修改日期')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user