#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from goods.models import Goods

# Create your models here.


class OrderForm(models.Model):
    order_number=models.CharField(max_length=20,verbose_name=u'订单编号')
    user=models.ForeignKey(UserProfile,verbose_name=u'用户')
    date=models.DateTimeField(auto_now=True,verbose_name=u'订单生成时间')
    isPay=models.BooleanField(default=False,verbose_name=u'是否支付')
    total=models.DecimalField(max_digits=6,decimal_places=2,verbose_name=u'总价')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'订单列表'
        verbose_name_plural=verbose_name


class OrderDatail(models.Model):
    goods=models.ForeignKey(Goods,verbose_name=u'商品')
    order=models.ForeignKey(OrderForm,verbose_name=u'订单')
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u'价格')
    count=models.IntegerField(verbose_name=u'数量')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'订单详情'
        verbose_name_plural=verbose_name