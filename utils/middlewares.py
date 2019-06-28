"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render, redirect, reverse
from Web_Django.settings import LOGINCHECK_LIST
import re

class LoginCheck(MiddlewareMixin):
    def process_request(self, request):
        self.req_path = request.path_info
        self.username = request.session.get('user')
        self.logincheck_list = LOGINCHECK_LIST
        request.bjm = 3

        # 黑名单url
        if self.req_path in self.logincheck_list['black']:
            return HttpResponse('<h1>该网页在黑名单</h1>', status=404)

        # 白名单url  or  已登录
        elif self.req_path in self.logincheck_list['white'] or self.re_white() or self.username:
            return None
        else:
            return redirect(reverse('app01:login') + '?next={}'.format(self.req_path))

    def process_view(self, request, view_func, view_argsm, view_kwargs):
        return None

    def process_response(self, request, response):
        return response

    def re_white(self):
        for re_url in self.logincheck_list['re_white']:
            if re.match(re_url, self.req_path):
                return True
        return False

if __name__ == '__main__':
    pass
