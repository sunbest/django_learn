# -*- coding: UTF-8 -*-

from django.http import HttpResponse  
from django.shortcuts import render 
from django.utils import timezone   


def index(request, template_name='index.html'): # 构建函数 接受request
    ip = request.META.get('REMOTE_ADDR')  # 从元信息中获取当前服务器ip地址
    now = timezone.now().strftime('%Y-%m-%d %H:%M:%S') # 按照 年-月-日 时：分：秒 格式化时间

    data = {} # 空字典
    if request.method == 'GET': # 判断请求是否是GET 方法
        return render(request, template_name, context={
            'ip': ip,
            'now': now,
            'data': data
        })# 把key "ip" ,"now","data" 通过渲染模板index.html显示values  这是GET方法的显示

    if request.method == 'POST': # 判断请求方法是否为POST方法
        name = request.POST.get('name', '') # 通过request.POST.get('name', '')获取表单key ”name“的值
        password = request.POST.get('password', '')#获取表单 key "password"的值
        like = request.POST.getlist('like', [])# 获取like的列表
        sex = request.POST.get('sex', '')#获取 表单 key "sex"的值
        fruit = request.POST.get('fruit', '')# 获取表单 key "fruit"的值

        data['name'] = name #构建字典 增加字典的key值为”name“ value 为表单传递name值
        data['password'] = password #构建字典 增加字典的key值为”password“ value 为表单传递password值
        data['like'] = like #构建字典 增加字典的key值为”like“ value 为表单传递like值
        data['sex'] = sex #构建字典 增加字典的key值为”sex“ value 为表单传递sexe值
        data['fruit'] = fruit #构建字典 增加字典的key值为”fruit“ value 为表单传递fruit值
        return render(request, template_name, context={
            'ip': ip,
            'now': now,
            'data': data
        })## 把key "ip" ,"now","data" 通过渲染模板index.html显示values 这是POST方法的显示
