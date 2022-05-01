from asyncio.windows_events import NULL
from dataclasses import fields
from re import L
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.views import View
from .models import Test
from django.core import serializers
from django.http import Http404
import json

# Create your views here.


class NoticeList(View):
    """
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
    """

    def get(self, requset):
        try:
            notice = Test.objects.all()
            if notice.count() == 0:
                raise Exception()
            else:
                data = serializers.serialize("json", list(
                    notice), fields=('num', 'title', 'writer'))
                return HttpResponse(data, content_type="text/json-comment-filtered")
        except Exception as e:
            raise Http404('게시글을 찾을 수 없습니다 다시 요청해주세요!')


class NoticeDetail(View):
    def get(self, requset, noticenum):
        noticedetail = get_list_or_404(Test, num=noticenum)
        data = serializers.serialize("json", noticedetail, fields=(
            'num', 'title', 'writer', 'content', 'file_url', 'date', 'img'))
        temp = json.loads(data)
        if(temp[0]['fields']['file_url'] != None):
            temp[0]['fields']['file_url'] = temp[0]['fields']['file_url'].split()
        if(temp[0]['fields']['img'] != None):
            temp[0]['fields']['img'] = temp[0]['fields']['img'].split()
        data = json.dumps(temp, indent=2, ensure_ascii=False)
        return HttpResponse(content=data)
    """
    class NoticeDetail(View):
        def get(self, requset, noticenum, major):
        noticedetail = get_list_or_404(Test,num = noticenum, major = major)
        data = serializers.serialize("json",noticedetail,fields = ('num','title','writer','content','file_url','date','img'))   
        temp = json.loads(data)
        if(temp[0]['fields']['file_url'] != None):
            temp[0]['fields']['file_url'] = temp[0]['fields']['file_url'].split()
        data = json.dumps(temp, indent=2, ensure_ascii=False)
        return HttpResponse(content=data)
    """
