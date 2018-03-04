from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^presentation/$', views.presentation, name='presentation'),
    url(r'^promos/$', views.promos, name='promos'),
    url(r'^reservation/$', views.reservation, name='reservation'),
    url(r'^reservation/1$', views.reservation1, name='reservation1'),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^test/$', views.test, name='test'),
    url(r'^promos/article/$', views.article_page, name='article_page'),

 

]

