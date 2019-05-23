"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

from django import template
register = template.Library()


@register.filter()
def add_str(value, string):
    return value + string


@register.simple_tag()
def join_str(*args):

    ret = ''

    for i in args:
        ret += str(i)

    return ret


@register.inclusion_tag(filename='inclusion_tags/pagination.html')
def pagination(page, now_page):
    return {'page_list': range(1, page+1), 'now_page': now_page}


@register.inclusion_tag(filename='inclusion_tags/left-menu.html')
def left_menu(select):
    return {'select': select}

if __name__ == '__main__':
    pass
