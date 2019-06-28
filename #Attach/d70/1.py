"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

import json
dictt = {'a': [1, 2], }


if __name__ == '__main__':
    q = json.dumps(dictt)
    print('aaa' + q + 'bbb')
    print(json.loads(q))
