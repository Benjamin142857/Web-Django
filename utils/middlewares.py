"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render, redirect, reverse
from Web_Django.settings import LOGINCHECK_LIST


class LoginCheck(MiddlewareMixin):
    def process_request(self, request):
        self.req_path = request.path_info
        self.username = request.session.get('user')

        if self.req_path in LOGINCHECK_LIST['black']:
            return HttpResponse('<h1>该网页在黑名单</h1>', status=404)
        elif self.req_path in LOGINCHECK_LIST['white'] or self.username:
            return None
        else:
            return redirect(reverse('app01:login') + '?next={}'.format(self.req_path))

    def process_view(self, request, view_func, view_argsm, view_kwargs):
        return None

    def process_response(self, request, response):
        return response


if __name__ == '__main__':
    pass
