#coding=utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger

from forms import LoginFrom,RegisterForm,ConsigneeForm
from models import UserProfile
from order.models import OrderDatail,OrderForm
from goods.models import Goods

# Create your views here.


def LoginView(request):
    login_form=LoginFrom(request.POST)
    if login_form.is_valid():
        post=request.POST
        user_name=post.get('username','')
        pass_word=post.get('password','')
        user=authenticate(username=user_name,password=pass_word)
        #uname = request.COOKIES.get('user_name', '')
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            # url=request.COOKIES.get('url','/')
            # red=HttpResponseRedirect(url)
            # request.session['user_id']=user_name[0].id
            # request.session['username']=user_name
            # return red
        else:
            return render(request,'users/login.html')
    else:
        return render(request,'users/login.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    register_form=RegisterForm(request.POST)
    if register_form.is_valid():
        post=request.POST
        user_name=post.get('user_name','')
        pass_word1=post.get('pwd','')
        pass_word2=post.get('cpwd','')
        if pass_word1 != pass_word2:
            return render(request,'users/register.html')
        email=post.get('email','')
        user_profile=UserProfile()
        user_profile.username=user_name
        user_profile.password=make_password(pass_word1)
        user_profile.email=email
        user_profile.save()
        return render(request,'users/login.html')
    else:
        return render(request,'users/register.html')


def register_user_existed(request):
    user_name=request.GET.get('user_name')
    count=UserProfile.objects.filter(username=user_name).count()
    return JsonResponse({'count':count})


def Info(request):
    goods_ids=request.COOKIES.get('goods_ids', '')
    if goods_ids!='':
        goods_ids1=goods_ids.split(',')
        goods_list=[]
        for goods_id in goods_ids1:
            goods_list.append(Goods.objects.get(id=int(goods_id)))
        context={'goods_list': goods_list}
        return render(request,'users/user_center_info.html',context)
    else:
        return render(request, 'users/user_center_info.html')


def site(request):
    site_form=ConsigneeForm(request.POST)

    if site_form.is_valid():
        post=request.POST
        site_name=post.get('name_receive','')
        site_address=post.get('address_receive','')
        site_zipcode=post.get('zipcode_receive','')
        site_mobile=post.get('mobile_receive','')
        receive = UserProfile.objects.get(username=request.user)
        receive.receive_name=site_name
        receive.receive_address=site_address
        receive.receive_zipcode=site_zipcode
        receive.receive_mobile=site_mobile
        receive.save()
        context={'receive':receive}
        return render(request,'users/user_center_site.html',context)
    else:
        receive1 = UserProfile.objects.get(username=request.user)
        context={'receive':receive1}
        return render(request,'users/user_center_site.html',context)


def order(request):
    order_goods=OrderForm.objects.filter(user=request.user)#获取该用户的所有订单
    #orde123=OrderForm.objects.filter(id=1)
    #a=OrderDatail.objects.filter(order_goods)
    #ordernum=order_goods.
    #all_goods=Goods.objects.all()
    #detail_goods=OrderDatail.objects.filter(pk=order_goods)
    detail_goods=OrderDatail.objects.all()#获得所有的详单
    #abc=order_goods

    #detail_goods=
    #detail_goods=all_goods.
    context={'order_goods':order_goods,'detail_goods':detail_goods}
    return render(request,'users/user_center_order.html',context)


def page_not_found(request):
    from django.shortcuts import render_to_response
    response=render_to_response('error/404.html',{})
    response.status_code=404
    return response


def page_error(request):
    from django.shortcuts import render_to_response
    response=render_to_response('error/500.html',{})
    response.status_code=500
    return response