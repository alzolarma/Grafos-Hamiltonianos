from django.conf.urls import patterns, url

from grafos import views

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    url(r'list/$', views.GrafoList.as_view(), name='plist'),
)