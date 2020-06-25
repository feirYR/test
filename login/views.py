from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    print('登陆成')
    return HttpResponse('测试录')