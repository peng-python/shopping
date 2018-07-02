from django.conf.urls import url
import views


urlpatterns=[
    url(r'^list/$',views.list),
    url(r'^detail/(?P<good_id>\d+)/$',views.detail),
    url(r'^search/$',views.search),
]