#coding=utf-8
from django.shortcuts import render,redirect
from django.db import transaction
from datetime import datetime
from decimal import Decimal

from users.models import UserProfile
from cart.models import Cart
from order.models import OrderForm,OrderDatail
# Create your views here.


def order(request):
    get=request.GET
    buyer=request.user
    receive=UserProfile.objects.get(username=buyer)
    receive_name=receive.receive_name
    receive_address=receive.receive_address
    receive_mobile=receive.receive_mobile
    # order_goods_id=post.get('good_cart_id','')#获得前端传过来的购物车的id
    # order_goods=Cart.objects.get(user=buyer)#查询出该购物车id中的所有商品
    cart_ids = get.getlist('good_cart_id','')
    cart_ids1 = [int(item) for item in cart_ids]
    order_goods = Cart.objects.filter(id__in=cart_ids1)
    context={'order_goods':order_goods,'receive_name':receive_name,
             'receive_address':receive_address,'receive_mobile':receive_mobile,
             'cart_ids':','.join(cart_ids)}
    return render(request,'order/place_order.html',context)


@transaction.atomic()
def submission(request):
    tran_id=transaction.savepoint()#记录当前的信息
    post=request.POST
    goods_carts_id=post.get('cart_ids')
    try:
        order_goods=OrderForm()
        now=datetime.now()
        buyer=request.user
        buyerid=buyer.id
        order_goods.order_number='%s%d'%(now.strftime('%Y%m%d%H%M%S'),buyerid)
        order_goods.user_id=buyerid
        order_goods.date=now
        order_goods.total=Decimal(post.get('total4'))
        order_goods.save()
        #创建订单详情
        #goods_carts_id1=[int(item) for item in goods_carts_id.split[',']]
                       # [int(item) for item in cart_ids.split[',']]
        goods_carts_id1 = [int(item) for item in goods_carts_id.split(',')]#此处split()将字符串分割成list
        #cart_ids1 = [int(item) for item in cart_ids]

        for id1 in goods_carts_id1:
            detail=OrderDatail()
            detail.order=order_goods
            carts=Cart.objects.get(id=id1)
            goods=carts.goods
            if goods.stock>=carts.count:
                goods.stock=goods.stock-carts.count
                goods.save()
                detail.goods_id=goods.id
                detail.price=goods.price
                detail.count=carts.count
                detail.save()
                carts.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart/')
    except Exception as e:
        print '==============%s'%e
        transaction.savepoint_rollback(tran_id)
    return redirect('/user/order/')

    #return render(request,'users/user_center_order.html')