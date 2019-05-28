from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from django.db.models import Max, Min, Avg, Sum, Count, Q, F
from app01 import models as app01
from utils import bjm



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'warning': ''})

    elif request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        next_path = request.GET.get('next')

        condition = Q(username=username) & Q(password=pwd)

        if app01.User.objects.filter(condition).exists():
            request.session['user'] = username
            request.session.set_expiry(3600 * 24 * 2)
            ret = redirect(next_path) if next_path else redirect(reverse('app01:press_list'))
        else:
            ret = render(request, 'login.html', {'warning': '用户名不存在或密码错误'})

        return ret

    else:
        return HttpResponse('error request methor', status=404)


def logout(request):
    request.session.delete()
    request.session.flush()
    ret = redirect(reverse('app01:login'))
    return ret


def test1(request, now_page='1'):
    page = 12
    print(now_page)
    now_page = int(now_page)
    temp_lst = [str(i)*3 for i in range(16)]

    if not now_page > page:
        ret_data = {
            'name': 'benjamin',
            'size': '12345678',
            'list': [temp_lst[i:i + 4] for i in range(len(temp_lst)) if i % 4 == 0],
            'page': page,
            'now_page': now_page,
        }
        ret = render(request, 'test1.html', ret_data)
    else:
        ret = HttpResponse('页面不存在', status=404)

    return ret


def test2(request, a):
    print(request.bjm)
    return HttpResponse('<h1>test2</h1>')


class Test3(View):
    def get(self, request, *args, a, b):
        print('执行test3[start]')
        ret = render(request, 'test3.html')
        print('执行test3[end]')

        return ret


# press - 出版社
def press_list(request):
    qs = app01.Press.objects.all()
    ret_data = {
        'press_qs': qs,
        'test': '2',
    }

    return render(request, 'press/press_list.html', ret_data)


def press_edit(request):
    press_id = request.GET.get('id')

    # 出版社编辑页面GET请求
    if request.method == 'GET':
        qs = app01.Press.objects.filter(id=press_id)
        # 判断是否存在此ID的出版社
        if len(qs) != 0:

            press_obj = qs[0]

            ret_data = {
                'id': press_obj.id,
                'name': press_obj.name,
            }

            ret = render(request, 'press/press_edit.html', ret_data)

        # 不存在此ID的出版社
        else:
            ret = HttpResponse('不存在此ID', status=404)

        return ret

    # 出版社已编辑更改信息POST请求
    elif request.method == 'POST':
        qs = app01.Press.objects.filter(id=press_id)
        # 判断是否存在此ID的出版社
        if len(qs) != 0:
            press_name = request.POST.get('press_name')

            press_obj = qs[0]
            press_obj.name = press_name
            press_obj.save()

            ret = redirect(reverse('app01:press_list'))

        # 不存在此ID的出版社
        else:
            ret = HttpResponse('不存在此ID', status=404)

        return ret

    else:
        return HttpResponse('错误非GET或POST请求', status=404)


def press_del(request):
    if request.method == 'GET':
        press_id = request.GET.get('id')

        qs = app01.Press.objects.filter(id=press_id)
        # 判断是否存在此ID的出版社
        if len(qs) != 0:
            press_obj = qs[0]
            press_obj.delete()

            ret = redirect(reverse('app01:press_list'))

        # 不存在此ID的出版社
        else:
            ret = HttpResponse('不存在此ID', status=404)

        return ret

    else:
        return HttpResponse('错误非GET请求', status=404)


def press_add(request):
    press_id = request.GET.get('id')

    # 出版社编辑页面GET请求
    if request.method == 'GET':
        ret = render(request, 'press/press_add.html')

        return ret

    # 出版社已编辑更改信息POST请求
    elif request.method == 'POST':
        press_name = request.POST.get('press_name')

        if press_name:
            app01.Press.objects.create(
                name=press_name,
            )

        ret = redirect(reverse('app01:press_list'))

        return ret

    else:
        return HttpResponse('错误非GET或POST请求', status=404)





if __name__ == '__main__':
    pass