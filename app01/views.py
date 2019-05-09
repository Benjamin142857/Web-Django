from django.shortcuts import render, HttpResponse, redirect
from app01 import models as app01

def login(request):
    return render(request, 'login.html')


def test(request):
    return redirect('/admin/')


def press_list(request):
    qs = app01.Press.objects.all()
    ret_data = {
        'press_qs': qs,
        'test': '2',
    }

    return render(request, 'press_list.html', ret_data)