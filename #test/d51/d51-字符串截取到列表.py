"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

import re


s = 'Benjamin 142857 hehe\r\nx=1\r\ny=2\r\nz=3\r\n\r\n又香又软的小泡芙'
lst0 = [
    ('Benjamin', 'love Stella'),
    ('Stella', 'love Benjamin'),
    ('Best', 'love huhuhu'),
]

if __name__ == '__main__':
    # lst1 = re.split('\\r\\n\\r\\n', s)
    # lst2 = re.split('\r\n\r\n', s)
    #
    # lst3 = re.split('\r\n', s)[0].split(' ')
    #
    # print(s)
    # print(lst1)
    # print(lst2)
    # print(lst3)

    # for循环跟else,若循环完整结束，即没遇到break,则执行else
    a = input('input someone name:\n')
    for i in lst0:
        if a in i:
            print(i[1])
            break

    else:
        print('no this people')
