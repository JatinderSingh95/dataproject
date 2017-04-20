from django.conf.urls import  url
from django.contrib import admin
from servers import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns =[
 
    url(r'^log/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	 url(r'^register/$', views.register, name='register'),
	  url(r'^img$', views.server_create2, name='server_img'),
  url(r'^$', views.server_list, name='server_list'),
  url(r'^new$', views.server_create, name='server_new'),
  url(r'^Article$', views.server_create1, name='server_new1'),
  url(r'^edit/(?P<pk>\d+)$', views.server_update, name='server_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
] 
