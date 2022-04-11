from dataclasses import fields
from re import L
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from .models      import Test
from django.core import serializers
import json

# Create your views here.

class NoticeList(View):
    def get(self, requset, majorname):
        notice = Test.objects.filter(major = majorname)
        data = serializers.serialize("json",list(notice),fields=('num','title','writer'))
        return HttpResponse(data,content_type="text/json-comment-filtered")
    
class NoticeDetail(View):
    def get(self, requset, noticenum, major):
        noticedetail = Test.objects.filter(num = noticenum, major = major)
        data = serializers.serialize("json",noticedetail,fields = ('num','title','writer','info','filename','fileurl'))   
        temp = json.loads(data)
        temp[0]['fields']['filename'] = temp[0]['fields']['filename'].split()
        data = json.dumps(temp, indent=2, ensure_ascii=False)
        return HttpResponse(content=data)
