from django.contrib import admin
from app.models import *


# Register your models here.
# 管理页面相关设置

class HeroInline(admin.StackedInline):
    model = [Book]
    extra = 2


class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'skill', 'english_name']
    list_per_page = 20  # 每页显示20条数据
    actions_on_bottom = True  # 下方也有操作框
    list_filter = ['name', 'skill']
    search_fields = ['name', 'skill']
    # fields = ['skill', 'name', 'hero_id']  # 修改/添加的时候字段排序
    fieldsets = (
        ('基本', {'fields': ['name']}),
        ('高级', {'fields': ['skill', 'hero_id']})
    )  # 标题分组
    # inlines = [HeroInline]


admin.site.register(Book)
admin.site.register(Hero, HeroAdmin)
