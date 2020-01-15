#!/usr/bin/env python
# coding: utf-8
class BaseResponse(object):
    """
    返回response
    """
    def __init__(self):
        self.code = 200
        self.data = None
        self.error = None

    @property
    def dict(self):
        return self.__dict__


'''
response = BaseResponse()  # 默认状态
object
    code:200    # 前端代码判断
    data:None    # 前端渲染页面
    error:None   # 前端错误展示

{'code':1000,'data':None,'error':None}
'''

CODE = {
    "200":"正常",
    "500":"登录失败",
    "501":"非法访问",
}