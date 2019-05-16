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


if __name__ == '__main__':
    pass
