from django.db import models


# Create your models here.  数据库
# 生成迁移  python3 manage.py makemigrations
# 执行迁移  python3 manage.py  migrate
# python3若需要变更数据库表的字段或者其他信息，需要重新生成迁移并执行才可生效。

# 测试 python3 manage.py shell
# from app.models import *
# b = Book()
# b.name = '白雪公主'
# b.save()
# print(Book.objects.all())
# print(Book.objects.get(name = '白雪公主')


class Book(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Hero(models.Model):
    name = models.CharField(max_length=20)
    skill = models.CharField(max_length=20, default='逃跑')
    hero_id = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
