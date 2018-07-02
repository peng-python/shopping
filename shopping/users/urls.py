from django.conf.urls import url
import views


urlpatterns=[
    url(r'^login/$',views.LoginView),
    url(r'^register/$',views.register),
    url(r'^register_user_existed/$',views.register_user_existed),
    url(r'^logout/$',views.Logout),
    url(r'^info/$',views.Info),
    url(r'^site/$',views.site),
    url(r'^order/$',views.order),
]