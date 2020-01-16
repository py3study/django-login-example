from django.shortcuts import render,HttpResponse, redirect,reverse
import time,json
from api import models
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

# Create your views here.
class UserlView(APIView):  # 用户表
    def post(self, request, *args, **kwargs):
        """
        post请求
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        print(name,pwd)
        # 查询表记录
        user_obj = models.User.objects.filter(username=name, password=pwd).first()
        if user_obj:
            # 更新登录时间
            user_obj.last_time = time.strftime('%Y-%m-%d %H:%M:%S')
            user_obj.save()
        else:
            # 返回 http 401
            return JsonResponse({'status': status.HTTP_401_UNAUTHORIZED, 'msg': 'Authentication failure'}, status=status.HTTP_401_UNAUTHORIZED)
        # 返回 http 200
        return JsonResponse({'status': status.HTTP_200_OK, 'data': []}, status=status.HTTP_200_OK)
