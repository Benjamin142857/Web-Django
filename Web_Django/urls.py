"""Web_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app01 import views as app01

urlpatterns = [
    # 后台管理
    path('admin/', admin.site.urls),


    # 出版社Press
    url(r'^press_list/', app01.press_list),
    url(r'^press_edit/', app01.press_edit),
    url(r'^press_del/', app01.press_del),
    url(r'^press_add/', app01.press_add),
    url(r'^login/', app01.login),


    # 临时测试
    path('test/', app01.test),
]
