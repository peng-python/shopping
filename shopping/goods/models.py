#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=20,verbose_name=u'分类')
    isDelete=models.BooleanField(default=False)
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'分类'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title


class Goods(models.Model):
    goods_type=models.ForeignKey(Category,verbose_name=u'分类')
    title=models.CharField(max_length=20,verbose_name=u'商品名称')
    image=models.ImageField(upload_to='goods/%Y/%m',max_length=100,verbose_name=u'商品图片')
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u'价格')
    isDelete=models.BooleanField(default=False)
    unit=models.CharField(max_length=20,default='500g',verbose_name=u'单位')
    click_nums=models.IntegerField(default=0,verbose_name=u'点击数')
    desc=models.CharField(max_length=300,verbose_name=u'商品简介')
    detail=models.TextField(verbose_name=u'商品详情')
    stock=models.IntegerField(verbose_name=u'库存')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'商品'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title




