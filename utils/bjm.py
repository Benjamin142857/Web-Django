"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
import os
import sys

import random


BJM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 定位到你的django根目录
sys.path.append(os.path.abspath(os.path.join(BJM_DIR, os.pardir)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web_Django.settings")

from app01 import models as app01
# import django
# django.setup()


def generate_id(length, info):
    TempDict = {'app01_book': (app01.Book.objects.all().values('book_id'), 'book_id')}
    temp_info = TempDict.get(info)

    if not temp_info:
        return None

    # 字符列表0~9, a~z
    char_list = [chr(i) for i in list(range(48, 58))+list(range(97, 123))]
    res_id = ''

    for i in range(length):
        res_id += random.choice(char_list)

    if ({temp_info[1]: res_id} in temp_info[0]) or (res_id == '0'*length):
        generate_id(length, info)
    else:
        return res_id


def get_page(page_str, max_page):
    try:
        page = int(page_str) if page_str else 1
        if page in range(1, max_page+1):
            return page
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    pass

