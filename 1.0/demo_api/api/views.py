from django.shortcuts import render,HttpResponse, redirect,reverse
from utils.response import BaseResponse,CODE
import time,json
from api import models
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
@csrf_exempt
def login(request):
    """
    登录验证
    :param request:
    :return:
    """
    response = BaseResponse()  # 初始化返回值
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        print(name, pwd)
        user_list = models.User.objects.filter(username=name, password=pwd)
        # response = {"state": False}
        if user_list:
            user_obj = user_list.first()
            # 设置session
            # request.session['username'] = name
            # request.session.set_expiry(3000)
            # 更新登录时间
            user_obj.last_time = time.strftime('%Y-%m-%d %H:%M:%S')
            user_obj.save()
        else:
            response.code = '500'
            response.data = CODE.get('500')
        return HttpResponse(json.dumps(response.__dict__))


    response.code = '501'
    response.data = CODE.get('501')
    return HttpResponse(json.dumps(response.__dict__))