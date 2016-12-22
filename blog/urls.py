# -*- coding:utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from blog.views import index,archive, article, comment_post,tag,category,do_login,do_logout,do_reg
from blog.upload import upload_image

urlpatterns = [
    url(r'^$', index, name='index'),
    # 映射到归档页面
    url(r'^archive/', archive, name='archive'),
    # 映射到文章页面
    url(r'^article/$', article, name='article'),
    # 映射到提交评论页面
    url(r'^comment/post/$', comment_post, name='comment_post'),
    # 映射到标签页面
    url(r'^tag/', tag, name='tag'),
    # 映射到分类页面
    url(r'^category/$', category, name='category'),
    # 登录注册注销
    url(r'^logout$', do_logout, name='logout'),
    url(r'^login$', do_login, name='login'),
    url(r'^reg$', do_reg, name='reg'),
]
