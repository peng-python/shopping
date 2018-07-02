#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,default='',verbose_name=u'昵称')
    mobile=models.CharField(max_length=11,null=True,blank=True,verbose_name=u'手机号码')
    address=models.CharField(max_length=100,default='',verbose_name=u'地址')
    receive_name=models.CharField(max_length=20,default='',verbose_name=u'收货人姓名')
    receive_address=models.CharField(max_length=100,default='',verbose_name=u'收货地址')
    receive_mobile=models.CharField(max_length=11,default='',verbose_name=u'收货手机号码')
    receive_zipcode=models.CharField(max_length=6,default='',verbose_name=u'邮政编码')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username


class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u'标题')
    image=models.ImageField(upload_to='banner/%Y/%m',max_length=100,verbose_name=u'轮播图')
    url=models.URLField(max_length=200,verbose_name=u'访问地址')
    index=models.IntegerField(default=100,verbose_name=u'顺序')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'轮播图'
        verbose_name_plural=verbose_name


    def __unicode__(self):
        return self.title