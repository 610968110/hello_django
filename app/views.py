from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect  # 重定向
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
    print("~~~~~~~~ -> %s" % request)
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


def create_book(request):
    book = Book()
    book.name = '三国演艺'
    book.save()
    # return HttpResponseRedirect('/book')  # 重定向
    return redirect('/book')


def login_check(request):
    # from django.http import QueryDict
    # d = QueryDict('a=1&a=2&b=3')
    # r = d['c']  # 抛异常
    # r1 = d.get('c')  # 返回空
    # r3 = d.get('a')  # 返回2
    # r4 = d.getlist('a')  # 返回 [1, 2]

    files = request.FILES  # 上传的文件
    cookie = request.COOKIES
    path = request.path  # 请求页面的完成路径，不包括域名和参数

    user_name = "null"
    user_pwd = ""

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_pwd = request.POST.get('user_pwd')
    elif request.method == 'GET':
        user_name = request.GET.get('user_name')
        user_pwd = request.GET.get('user_pwd')

    if user_name == user_pwd:

        response = HttpResponse("设置cookie")
        response.set_cookie('user_name', user_name, max_age=60)  # 60秒过期  expires是具体时间需要用datetime去实现
        return JsonResponse({'code': 200, 'message': "login success"})
    else:
        return JsonResponse({'code': 500, 'message': "login err"})


def cookie(request):
    cookie = request.COOKIES
    user_name = ""
    if 'user_name' in cookie:
        user_name = cookie.get('user_name')


def session(request):
    request.session['user_name'] = 'root'  # 默认是14天
    user_name = request.session['user_name']
    del request.session['user_name']
    request.session.clear()
    request.session.set_expiry(60)  # 单位：秒，设置sessionId的过期时间,0关闭浏览器就失效
