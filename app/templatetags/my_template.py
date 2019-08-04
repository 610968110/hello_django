from django.template import Library

register = Library()


@register.filter
def mod(num, change_count):
    """
    自定义模板过滤 需要在setting中设置 libraries
    至少有一个参数 最多两个参数，|前面的是第一个参数，用:传入剩下的参数
    """
    return num % change_count == 0
