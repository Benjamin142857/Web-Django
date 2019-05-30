"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

dictt = {'a': [1, 2], }


if __name__ == '__main__':
    qqq = dictt['a']
    dictt['a'] = [3, 4, 5]
    qqq.append(6)
    print(dictt)
