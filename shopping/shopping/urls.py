#coding=utf-8
"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from goods.views import IndexView
from shopping.settings import MEDIA_ROOT
from django.views.static import serve


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^user/',include('users.urls')),
    url(r'^goods/',include('goods.urls')),
    url(r'^cart/',include('cart.urls')),
    url(r'^order/',include('order.urls')),
    #处理上传文件的路径
    url(r'^media/(?P<path>.*$)',serve,{'document_root':MEDIA_ROOT}),
]


handler404='users.views.page_not_found'
handler500='users.views.page_error'