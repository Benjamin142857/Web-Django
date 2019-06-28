from django import forms
from django.forms import Form, widgets
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


# 注册表Form
class RegForm(Form):
    username = forms.CharField(
        min_length=4,
        max_length=16,
        label='用户名',
        error_messages={
            'min_length': '用户名不能少于4位字符',
            'max_length': '用户名最长为16个字符',
            'required': '用户名不能为空',
        },
        widget=widgets.TextInput(attrs={'rm-error': 'true'})
    )
    password = forms.CharField(
        min_length=8,
        max_length=16,
        label='密码',
        error_messages={
            'min_length': '密码不能少于8位字符',
            'max_length': '密码最长为16个字符',
            'required': '密码不能为空',
        },
        widget=widgets.PasswordInput(attrs={'rm-error': 'true'})
        # widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请填写密码'})
    )
    re_password = forms.CharField(
        label='确认密码',
        error_messages={
            'required': '密码不能为空',
        },
        widget = widgets.PasswordInput(attrs={'rm-error': 'true'})
        # widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '确认密码'})
    )
    gender = forms.ChoiceField(
        label='性别',
        choices=(('0', '保密'), ('1', '男'), ('2', '女')),
        widget=widgets.RadioSelect,
    )

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type in ['text', 'password']:
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['style'] = "background: rgba(255, 255, 255, 0.7);"

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if models.User.objects.filter(username=username).exists():
            raise ValidationError('用户名已存在')
        else:
            return username

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')

        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码不一致')