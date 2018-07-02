import xadmin

from models import Category,Goods


class CategoryAdmin(object):
    list_display=['title','isDelete','add_time']
    search_fields=['title','isDelete']
    list_filter=['title','isDelete','add_time']


class GoodAdmin(object):
    list_display=['goods_type','title','image','price','isDelete','unit','click_nums',
                  'desc','detail','stock','add_time']
    search_fields=['goods_type','title','image','price','isDelete','unit','click_nums',
                  'desc','detail','stock']
    list_filter=['goods_type','title','image','price','isDelete','unit','click_nums',
                  'desc','detail','stock','add_time']


xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Goods,GoodAdmin)