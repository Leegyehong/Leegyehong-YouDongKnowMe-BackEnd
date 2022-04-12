from dataclasses import fields
from re import L
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from django.views import View 
from .models      import Test
from django.core import serializers
from django.http import Http404
import json

# Create your views here.

class NoticeList(View):
    def get(self, requset, majorname):
        try:
            notice = Test.objects.filter(major = majorname)
            if notice.count() == 0:
                raise Exception() 
            else :
                data = serializers.serialize("json",list(notice),fields=('num','title','writer'))
                return HttpResponse(data,content_type="text/json-comment-filtered")
        except Exception as e:
            raise Http404('게시글을 찾을 수 없습니다 다시 요청해주세요!')  
        
    
class NoticeDetail(View):
    def get(self, requset, noticenum, major):
        noticedetail = get_list_or_404(Test,num = noticenum, major = major)
        data = serializers.serialize("json",noticedetail,fields = ('num','title','writer','info','filename','fileurl'))   
        temp = json.loads(data)
        temp[0]['fields']['filename'] = temp[0]['fields']['filename'].split()
        data = json.dumps(temp, indent=2, ensure_ascii=False)
        return HttpResponse(content=data)
