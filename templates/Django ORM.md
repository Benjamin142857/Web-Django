# Django ORM

> Author : Benjamin142857
>
> Date : 2019-05-14
>
> [TOC]



![](http://www.benjamin-stella.cn/logo.png)



## 1. Django ORM Mapping

Django里是用一种其他的方式连接SQL，而不需自己写，自己写SQL虽也不难，但会有以下问题：

- 被sql 注入
- 代码与sql写死在一起，导致解耦差
- 开发人员的sql水平不一，导致性能问题
- 开发效率低

对象关系映射ORM（Object Relational Mapping），它的实质就是将关系数据库中的业务数据用对象的形式表示出来，并通过面向对象的方式将这些对象组织起来，实现系统业务逻辑的过程。

在ORM过程中最重要的概念是映射（Mapping），通过这种映射可以使业务对象与数据库分离。从面向对象来说，数据库不应该和业务逻辑绑定在一起，ORM则起到这样的分离作用，使数据库层透明，开发人员真正地面向对象。



### 1.1 Mapping数据类型

| 数据类型                  | 说明                       |
| ------------------------- | -------------------------- |
| AutoField                 | 自增                       |
| BigAutoField              | 大自增                     |
| SmallIntegerField         | 小整形$[-2^{15},2^{15}-1]$ |
| IntegerField              | 整型$[-2^{31},2^{31}-1]$   |
| BigIntegerField           | 大整型$[-2^{63},2^{63}-1]$ |
| PositiveSmallIntegerField | 正小整型$[0,2^{16}-1]$     |
| PositiveIntegerField      | 正整形 $[0,2^{32}-1]$      |
| FloatField                | 浮点型                     |
| DecimalField              | 十进制                     |
| BinaryField               | 二进制                     |
| BooleanField              | 布尔                       |
| NullBooleanField          | 支持空字符的布尔           |
| CharField                 | 字符串                     |
| TextField                 | 长字符串                   |
| DataField                 | 2018-7-21                  |
| DataTimeField             | 2018-7-21      15:51:21    |
| DurationField             | 区间 [a, b]                |
| EmailField                | 存储Email格式              |
| FileField                 | 存储文件                   |
| ImageField                | 图片                       |
| SlugField                 | 标签                       |
| URLField                  | URL地址                    |
| GenericIPAddressField     | IP地址，支持ipv4           |
| UUIDField                 | UUID编码                   |



### 1.2 Mapping常用参数


| 内部可选                                                     | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| verbose_name=“Label” 或直接                          “Label” | 备注，备注了的数据类型在admin里会以备注的形式展示，而不是变量名 |
| max_length = (intnum)                                        | 最大长度                                                     |
| unique = (True/False)                                        | 是否不可重复                                                 |
| null = (True/False)                                          | 是否可以为空                                                 |
| blank = (True/False)                                         | 在Admin中是否可以为空                                        |
| primary_key = (True/False)                                   | 是否此表格独立属性，即多个表格间可能有相同属性如 “id”，此时就需要(primary_key=True) |
| auto_now_add = (True/False)                                  | 是否自动添加，一般用于日期                                   |
| on_delete = (models.CASCADE)                                 | 立遗：外键关联删除关系                                       |





## 2. 单表的增删改查

### 2.1 一般数据的查询

~~~python
"""
以 Account 账户表为例
"""

# 获取Account表格 所有数据对象的 QuerySet
models.Account.objects.all()

# get 条件筛选（直接返回数据对象，不常用，因为当不存在符合条件的数据，或符合条件的数据不止一条，会报错）
models.Account.objects.get(id='123456')		# 筛选id='123456'的数据

# filter 条件筛选（返回符合条件的数据对象的 QuerySet，若没有符合条件的数据，返回空 QuerySet）
models.Account.objects.filter(id='123456')						# id='123456'
models.Account.objects.filter(id='123456', passwd='123456')		# id='123456' 且 passwd='123456'
    
    
# filter 区间筛选
models.Account.objects.filter(money__gt=100) # money > 100
models.Account.objects.filter(money__gte=100) # money >= 100
models.Account.objects.filter(money__lt=100) # money < 100
models.Account.objects.filter(money__lte=100) # money <= 100
models.Account.objects.filter(money__rang(100, 150)) # 100 <= money < 150

# filter 字符串筛选
models.Account.objects.filter(passwd_startswith='a') # 以a开头的passwd，大小写敏感
models.Account.objects.filter(passwd_istartswith='a') # 以a/A开头的passwd，大小写不敏感
models.Account.objects.filter(passwd_endswith='a') # a结尾的passwd，大小写敏感
models.Account.objects.filter(passwd_iendswith='a') # a/A结尾的passwd，大小写不敏感
models.Account.objects.filter(username_contains='a') # 包含a的username(大小写敏感)
models.Account.objects.filter(username_icontains='a') # 包含a/A 的username(大小写不敏感)
models.Article.objects.filter(title__regex=r'xxxxxxx') # 正则表达查找（大小写敏感）
models.Article.objects.filter(title__iregex=r'xxxxxxx') # 正则表达查找（大小不写敏感）

# filter 多数据列表筛选
models.Account.objects.filter(id__in=[1, 3, 12]) # 把id=1, 3, 12的取出来

# filter 空值筛选
models.Article.objects.filter(tags_isnull=True) # tags是空的（tags=NULL）

# exclude 反选查询
models.Account.objects.exclude('条件')   # 排除符合条件的数据，与filter相反
~~~



### 2.2 时间数据的查询

~~~python
"""
针对于 DataField 与 DataTimeField 的查询
以 Account.register_date  账户表中用户的注册时间为例
"""

# 精确日期查找（具体到秒的某一时刻）
models.Account.objects.filter(register_date__date = datetime.datetime(2019, 5, 14, 21, 34, 52))   # 【2019-05-14 21:34:52】


#日期区间查找#
# 精确到日 【2005-01-01 00:00:00】 ~ 【2005-03-31 00:00:00】
models.Account.objects.filter(register_date__rang('2005-01-01', '2005-03-31'))	
# 精确到秒 【2019-05-14 21:34:52】 ~ 【2019-05-14 21:35:55】
models.Account.objects.filter(register_date__rang(datetime.datetime(2019, 5, 14, 21, 34, 52), datetime.datetime(2019, 5, 14, 21, 35, 55))) 
# [大于/小于/大于等于/小于等于] 只需将rang换成 [gt/lt/gte/lte]

# 特殊条件查询
models.Account.objects.filter(register_date__year = 2018)   # 查2018年
models.Account.objects.filter(register_date__month = 5) # 查所有年里5月份的
models.Account.objects.filter(register_date__day/hour/minute/second = ) # 查日分时秒
models.Account.objects.filter(register_date__week = 52) # 查一年中第52周的
models.Account.objects.filter(register_date__week_day = 2) # 查周二(1-7对应sunday-saturday)
~~~







## 3. 外键关联的增删改查





## 4. 多对多关联的增删改查







## 5. QuerySet 对象常用方法

### 5.1 QuerySet 批量删改

~~~python
"""
以 Account 账户表为例
"""

# 将 id > 10 的用户全删了
qs = models.Account.objects.filter(id__gt=10)
qs.delete()  

# 将 id > 10 的用户密码全改为 ‘123456’,money改为 100
qs = models.Account.objects.filter(id__gt=10)
qs.update(passwd='123456', money=100)
~~~





## 5.2 QuerySet 进一步查询

