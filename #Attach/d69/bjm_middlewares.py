"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MD001(MiddlewareMixin):
    def process_request(self, request):
        request.bjm = 'Benjamin142857'
        print('MD001 - process_request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('MD001 - process_view [start]')
        print(view_func, view_args, view_kwargs)
        print('MD001 - process_view [end]')

    def process_exception(self, request, exception):
        print('MD001-error : {}'.format(exception))
        return HttpResponse('MD001-error : {}'.format(exception))

    def process_response(self, request, response):
        print('MD001 - process_response')
        return response

    def process_template_response(self, request, response):
        print('MD001 - process_template_response')
        return response


class MD002(MiddlewareMixin):
    def process_request(self, request):
        print('MD002 - process_request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('MD002 - process_view [start]')
        print(view_func, view_args, view_kwargs)
        print('MD002 - process_view [end]')

    def process_exception(self, request, exception):
        print('MD002-error : {}'.format(exception))
        return HttpResponse('MD002-error : {}'.format(exception))

    def process_response(self, request, response):
        print('MD002 - process_response')
        return response

    def process_template_response(self, request, response):
        print('MD002 - process_template_response')
        return response



# class MD003(MiddlewareMixin):
#     def process_request(self, request):
#         print('MD003 - process_request')


if __name__ == '__main__':
    pass
