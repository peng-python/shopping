#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from goods.models import Goods

# Create your models here.


class Cart(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name=u'用户')
    goods=models.ForeignKey(Goods,null=True,blank=True,verbose_name=u'购买的商品')
    count=models.IntegerField()
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'购物车'
        verbose_name_plural=verbose_name