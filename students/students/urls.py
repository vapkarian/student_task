from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'students.views.home', name='home'),
    # url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
                       url(r'^accounts/login/$',login),
                       url(r'^accounts/logout/$',logout),
                       url(r'^admin/',include(admin.site.urls)),
                       url(r'^groups/(\d+)/$','studentgroups.views.group_detail'),
                       url(r'^groups/$','studentgroups.views.group_list'),
                       url(r'^$','students.views.index'),
)
