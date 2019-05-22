"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
import time

def timer(fn):
    def inner(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        print('use time:{}'.format(time.time()-start))

    return inner

@timer
def setinterval(s):
    time.sleep(s)


if __name__ == '__main__':
    setinterval(1)
