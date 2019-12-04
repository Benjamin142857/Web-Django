"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

import requests

if __name__ == '__main__':
    url = 'http://172.22.1.175/di/http.action?userId=idc&pwd=9rRXNr&interfaceId=getSurfAwstMRainTimeRange4Iiiii&dataFormat=json&iiiii=G1810&s_ymdhms=20190710150000&e_ymdhms=20190710174300'
    req = requests.request(
        url=url,
        method='get',
    )
    dict1 = req.json()
    print(dict1)
