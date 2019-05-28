from django.urls import path, re_path
from django.conf.urls import url
from app01 import views as app01

app_name = 'app01'

urlpatterns = [
    # 出版社Press
    url(r'^press_list/', app01.press_list, name='press_list'),
    url(r'^press_edit/', app01.press_edit, name='press_edit'),
    url(r'^press_del/', app01.press_del, name='press_del'),
    url(r'^press_add/', app01.press_add, name='press_add'),
    url(r'^login/', app01.login, name='login'),
    url(r'^logout/', app01.logout, name='logout'),

    # 临时测试
    url(r'^test1/$', app01.test1),
    url(r'^test1/(?P<now_page>[0-9]+)/$', app01.test1),
    url(r'^test2/(?P<a>[0-9a-z]{3})/$', app01.test2),
    url(r'^test3/(?P<a>[0-9a-z]{1})/(?P<b>[0-9a-z]{2})/([0-9a-z]{3})/$', app01.Test3.as_view())
]
