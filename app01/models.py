from django.db import models


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

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)

    class Meta:
        verbose_name_plural = '出版社表'


#