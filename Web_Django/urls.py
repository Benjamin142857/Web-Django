from django.contrib import admin
from django.urls import path, re_path, reverse
from django.conf.urls import url, include
from app01 import views as app01


urlpatterns = [
    # 后台管理
    path('admin/', admin.site.urls),


    # app01
    url(r'^app01/', include('app01.urls', namespace='app01')),


]
