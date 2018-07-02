#coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger

from users.models import Banner
from goods.models import Goods,Category

# Create your views here.


class IndexView(View):
    def get(self,request):
        #user_name=request.get('user_name')
        banners=Banner.objects.all().order_by('index')[:4]
        category_list=Category.objects.all()
        fruits=category_list[0].goods_set.order_by('-id')[:4]
        fruits_hot=category_list[0].goods_set.order_by('-click_nums')[:4]
        seafoods=category_list[1].goods_set.order_by('-id')[:4]
        seafoods_hot=category_list[1].goods_set.order_by('-click_nums')[:4]
        muttons=category_list[2].goods_set.order_by('-id')[:4]
        muttons_hot=category_list[2].goods_set.order_by('-click_mums')[:4]
        eggs=category_list[3].goods_set.order_by('-id')[:4]
        eggs_hot=category_list[3].goods_set.order_by('-click_nums')[:4]
        vegetables=category_list[4].goods_set.order_by('-id')[:4]
        vegetables_hot=category_list[4].goods_set.order_by('-click_nums')[:4]
        freezes=category_list[5].goods_set.order_by('-id')[:4]
        freezes_hot=category_list[5].goods_set.order_by('-click_nums')[:4]

        context={'banners':banners,
                 'fruits':fruits,'fruits_hot':fruits_hot,'seafoods':seafoods,'seafoods_hot':seafoods_hot,
                 'muttons': muttons, 'muttons_hot': muttons_hot,'eggs':eggs,'eggs_hot':eggs_hot,
                 'vegetables':vegetables,'vegetables_hot':vegetables_hot,
                 'freezes':freezes,'freezes_hot':freezes_hot}
        return render(request,'goods/index.html',context)


def list(request):
    get_goods=request.GET
    all_categorys=Category.objects.all()#获得所有分类
    category_id=get_goods.get('category','')#得到前端传过来的分类id
    all_goods = Goods.objects.filter(goods_type=int(category_id))#查询该分类下所有的商品
    category=all_categorys.get(pk=int(category_id))#获取该分类的名称
    new_goods=all_goods.order_by('-id')[:2]#获得最新的两个

    # search_keywords=get_goods.get('keywords','')
    # if search_keywords:
    #     all_goods=Goods.objects.all()
    #     all_goods=all_goods.filter(Q(title__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))


    sort=get_goods.get('sort','')
    if sort:
        if sort=='price_sort':
            all_goods=all_goods.order_by('price')
        if sort=='click':
            all_goods=all_goods.order_by('-click_nums')
    try:
        page=request.GET.get('page','1')
    except PageNotAnInteger:
        page=1
    p=Paginator(all_goods,1,request=request)
    goods=p.page(page)
    context={'all_goods':goods,'category_id':category_id,'category':category,
             'sort':sort,'new_gooods':new_goods}
    return render(request,'goods/list.html',context)


def detail(request,good_id):
    goods=Goods.objects.get(id=int(good_id))
    goods.click_nums+=1
    goods.save()
    category=goods.goods_type
    context={'goods':goods,'category':category}
    #return render(request,'goods/detail.html',context)
    response=render(request,'goods/detail.html',context)

    #记录浏览记录
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_id='%d'%goods.id
    if goods_ids!='':
        goods_ids1=goods_ids.split(',')
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>=6:
            del goods_ids1[5]
        goods_ids=','.join(goods_ids1)
    else:
        goods_ids=goods_id
    response.set_cookie('goods_ids',goods_ids)
    return response


def search(request):
    get_goods=request.GET
    all_goods=Goods.objects.all()
    search_keywords = get_goods.get('keywords', '')
    new_goods = all_goods.order_by('-id')[:2]
    if search_keywords:
        all_goods = Goods.objects.all()
        all_goods = all_goods.filter(Q(title__icontains=search_keywords) | Q(desc__icontains=search_keywords) | Q(
            detail__icontains=search_keywords))
    sort = get_goods.get('sort', '')
    if sort:
        if sort == 'price_sort':
            all_goods = all_goods.order_by('price')
        if sort == 'click':
            all_goods = all_goods.order_by('-click_nums')
    try:
        page = request.GET.get('page', '1')
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_goods, 1, request=request)
    goods = p.page(page)
    context = {'all_goods': goods, 'sort': sort, 'new_gooods': new_goods}
    return render(request, 'goods/list.html', context)