from django.http import HttpResponse

def index(request):
    """
    视图   函数视图
    :param request:请求对象，包含了请求信息的一个请求对象
    :return:
    """
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('这是about页面')