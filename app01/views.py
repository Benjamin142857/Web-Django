from django.shortcuts import render, HttpResponse, redirect
from app01 import models as app01


def login(request):
    return render(request, 'login.html')


def test(request):
    ret_data = {
        'name': 'benjamin'
    }
    return render(request, 'test.html', ret_data)


# press - 出版社
def press_list(request):
    qs = app01.Press.objects.all()
    ret_data = {
        'press_qs': qs,
        'test': '2',
    }

    return render(request, 'press_list.html', ret_data)


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

            ret = render(request, 'press_edit.html', ret_data)

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

            ret = redirect('/press_list/')

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

            ret = redirect('/press_list/')

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
        ret = render(request, 'press_add.html')

        return ret

    # 出版社已编辑更改信息POST请求
    elif request.method == 'POST':
        press_name = request.POST.get('press_name')

        if press_name:
            app01.Press.objects.create(
                name=press_name,
            )

        ret = redirect('/press_list')

        return ret

    else:
        return HttpResponse('错误非GET或POST请求', status=404)





if __name__ == '__main__':
    pass