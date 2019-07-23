from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from app.models import *


# from  django.http import ques


# Create your views here.


def index0(request):
    # p = Question.objects.order_by('-pub_time')
    # 加载模板文件
    temp = loader.get_template('index.html')
    # 定义上下文，给模板传递参数
    context = {'key': '我是传进来的数据'}
    # 渲染模板
    html = temp.render(context)
    return HttpResponse(html)


def index(request):
    """模板"""
    return render(request, "index.html", {'key': '啦啦啦', 'list': [1, 2, 3, 4, 5]})


def index1(request):
    """视图"""
    return HttpResponse('123')


def index2(request):
    """视图"""
    return HttpResponse('456')


def show_book(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})


def show_hero(request, book_id):
    book = Book.objects.get(id=book_id)
    hero = book.hero_set.all()
    return render(request, 'hero.html', {'hero': hero})
