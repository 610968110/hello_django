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

    # class Meta:
    #     db_table = 'Book'


class Hero(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    skill = models.CharField(verbose_name='技能', max_length=20, default='逃跑')
    hero_id = models.ForeignKey('Book', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='icon')  # 上传到那个路径，路径是相对于media文件夹

    def __str__(self):
        return self.name

    def english_name(self):
        return self.name

    # 排序相关
    name.admin_order_field = 'name'
    skill.admin_order_field = 'skill'
    english_name.admin_order_field = 'name'

    # 重命名相关
    english_name.short_description = '英文名'
