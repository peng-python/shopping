#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse

from models import Cart
from goods.models import Goods

# Create your views here.


def add(request,good_id,count):
    buyers=request.user#获得当前用户
    #buy_goods=Goods.objects.get(id=int(good_id))#购买的商品
    buy_count=int(count)
    goods_cart=Cart.objects.filter(user=buyers,goods_id=int(good_id))
    if len(goods_cart)>=1:#如果商品存在
        buy_cart=goods_cart[0]
        buy_cart.count=buy_cart.count+buy_count
    else:
        buy_cart=Cart()
        buy_cart.user=buyers
        buy_cart.goods_id=good_id
        buy_cart.count=buy_count
    buy_cart.save()
    if request.is_ajax():
        count=Cart.objects.filter(user=buyers)
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')


def cart(request):
    buyers=request.user
    goods_cart=Cart.objects.filter(user=buyers)
    context = {'goods_cart': goods_cart}
    return render(request, 'cart/cart.html', context)


def modify(request,goodcart_id,count):#在购物车中进行增加或者减少商品数量的处理，ajax与cart.html页面的93行左右交互
    try:
        good_cart=Cart.objects.get(id=int(goodcart_id))
        count1=good_cart.count=int(count)
        good_cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok',count1}
    return JsonResponse(data)


def delete(request,goodcart_id):
    try:
        good_cart=Cart.objects.get(id=int(goodcart_id))
        good_cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)