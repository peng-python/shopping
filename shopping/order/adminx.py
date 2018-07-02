import xadmin

from models import OrderForm,OrderDatail


class OrderformAdmin(object):
    list_display=['order_number','user','date','isPay','total','add_time']
    search_fields=['order_number','user','date','isPay','total']
    list_filter=['order_number','user','date','isPay','total','add_time']


class OrderdatailAdmin(object):
    list_display=['goods','order','price','count','add_time']
    search_fields=['goods','order','price','count']
    list_filter=['goods','order','price','count','add_time']


xadmin.site.register(OrderForm,OrderformAdmin)
xadmin.site.register(OrderDatail,OrderdatailAdmin)