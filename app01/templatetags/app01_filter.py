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
def join_str(*args, **kwargs):
    print(args)
    print(kwargs)

    ret = ''

    for i in args:
        ret += str(i)

    return ret


if __name__ == '__main__':
    pass
