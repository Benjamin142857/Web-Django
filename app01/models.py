from django.db import models
from utils import bjm
import random


# 用户表
class User(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return '{}-{}'.format(self.id, self.username)

    class Meta:
        verbose_name_plural = '用户表'


# 出版社表
class Press(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=32)
    aaa = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

    class Meta:
        verbose_name_plural = '出版社表'


# 书籍表
class Book(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    book_id = models.CharField(max_length=12, default=random.choice(['111', '222', '333']))
    name = models.CharField(max_length=32)
    press = models.ForeignKey(to='Press', on_delete=models.SET_NULL, null=True, blank=True, related_name='book')
    price = models.IntegerField()
    pub_date = models.DateField()

    def __str__(self):
        return '{}-{}'.format(self.book_id, self.name)

    class Meta:
        verbose_name_plural = '书籍表'
