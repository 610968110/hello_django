from django.contrib import admin
from app.models import *


# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'skill']


admin.site.register(Book)
admin.site.register(Hero, HeroAdmin)
