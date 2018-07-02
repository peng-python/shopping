import xadmin

from models import Cart


class CartAdmin(object):
    list_display=['user','goods','count','add_time']
    search_fields=['user','goods','count']
    list_filter=['user','goods','count','add_time']


xadmin.site.register(Cart,CartAdmin)