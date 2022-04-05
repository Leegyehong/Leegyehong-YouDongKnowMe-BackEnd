from dataclasses import fields
from re import L
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models      import Test
from django.core import serializers

# Create your views here.

class NoticeList(View):
    def get(self, requset, majorname):
        notice = Test.objects.filter(major = majorname)
        data = serializers.serialize("json",list(notice),fields=('num','title','writer'))
        return HttpResponse(data,content_type="text/json-comment-filtered")
    
class NoticeDetail(View):
    def get(self, requset, noticenum, major):
        noticedetail = Test.objects.filter(num = noticenum, major = major)
        data = serializers.serialize("json",list(noticedetail),fields = ('num','title','writer','info','filename','fileurl'))   
        return HttpResponse(content=data)
