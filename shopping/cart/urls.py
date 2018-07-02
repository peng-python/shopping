from django.conf.urls import url
import views


urlpatterns=[
    url(r'^$',views.cart),
    url(r'^add/(\d+)_(\d+)/$',views.add),
    url(r'^modify(\d+)_(\d+)/$',views.modify),
    url(r'^delete(\d+)/$',views.delete),
]