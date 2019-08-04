from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIpsMiddleWare(MiddlewareMixin):
    BLOCK_IPS = ['192.168.1.1']

    """
    
    中间键类 ,拦截指定ip禁止访问
    需要在setting文件中注册中间件类
    """

    def __init__(self, get_response):
        print('__init__')
        self.get_response = get_response

    # def __call__(self, request):
    #     # 从这结束请求到视图前执行的语句
    #     response = self.get_response(request)
    #     return response

    def process_request(self, request):
        print('process_request')
        return None

    def process_view(self, request, view_func, *args, **kwargs):
        """
        视图函数调用之前会调用
        名字只能叫 process_view ，参数只能是这些
        view_func 为函数名，自己在views.py里写
        """
        print('process_view')
        if request.META['REMOTE_ADDR'] in BlockedIpsMiddleWare.BLOCK_IPS:  # 访问者浏览器的ip
            return HttpResponse('你在黑名单里')  # 如果在黑名单里，直接返回禁止访问的结果

    def process_response(self, request, response):
        print('process_response')
        return response

    def process_exception(self, request, exception):
        print('process_exception')
        return HttpResponse("in exception")


# __init__:服务器响应第一个请求的时候调用。比如服务器重启之后接收第一个请求时调用
# process_request:是在产生request对象，进行url匹配之前调用。
# process_view：是url匹配之后，调用视图函数之前。
# process_response：视图函数调用之后，内容返回给浏览器之前。
# process_exception:视图函数出现异常，会调用这个函数。
# 如果注册的多个中间件类中包含process_exception函数的时候，调用的顺序跟注册的顺序是相反的。


"""
顺序：
浏览器请求 -> 产生request对象 -> process_request  -> url配置 -> process_view -> 调用view -> 
process_response -> 返回给浏览器

"""
