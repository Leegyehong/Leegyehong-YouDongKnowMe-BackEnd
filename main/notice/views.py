from dataclasses import fields
from re import L
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import Noti
from django.core import serializers
from django.http import Http404
from http import HTTPStatus

import json

# Create your views here.


class NoticeList(View):
    """
    def get(self, requset, majorname):
        try:
            notice = Noti.objects.filter(major = majorname)
            if notice.count() == 0:
                raise Exception() 
            else :
                data = serializers.serialize("json",list(notice),fields=('num','title','writer'))
                return HttpResponse(data,content_type="text/json-comment-filtered")
        except Exception as e:
            raise Http404('게시글을 찾을 수 없습니다 다시 요청해주세요!')  
    """

    def get(self, requset):
        pass
        try:
            notice = Noti.objects.using('crawled_data').all().order_by('-num')
            if notice.count() == 0:
                raise Exception()
            else:
                data = serializers.serialize("json", list(
                    notice), fields=('num', 'title','date', 'writer'))
                return HttpResponse(data, content_type="text/json-comment-filtered")
        except Exception as e:
            return JsonResponse({'message':'error'},status=HTTPStatus.BAD_REQUEST)
            #raise JS('게시글을 찾을 수 없습니다 다시 요청해주세요!')


class NoticeDetail(View):

    def get(self, requset, noticenum):
        noticedetail = Noti.objects.using('crawled_data').filter(num=noticenum).order_by('-num')
        data = serializers.serialize("json", noticedetail, fields=(
            'num', 'title', 'writer', 'content', 'file_url', 'date', 'img_url'))
        temp = json.loads(data)
        print(temp)
        if(temp[0]['fields']['file_url'] != None):
            temp[0]['fields']['file_url'] = temp[0]['fields']['file_url'].split()
        if(temp[0]['fields']['img_url'] != None):
            temp[0]['fields']['img_url'] = temp[0]['fields']['img_url'].split()
            
        # 메서드화 필요
        if not temp[0]['fields']['content']:
            temp[0]['fields']['content'] = ""
        temp[0]['fields']['content']=temp[0]['fields']['content'].replace(" ", "")
        
        if not temp[0]['fields']['file_url']:
            temp[0]['fields']['file_url'] = ""
        
        
        if not temp[0]['fields']['img_url']:
            temp[0]['fields']['img_url'] = ""
        
        data = json.dumps(temp, indent=2, ensure_ascii=False)
        return HttpResponse(content=data)
    """
    class NoticeDetail(View):
        def get(self, requset, noticenum, major):
        noticedetail = get_list_or_404(Noti,num = noticenum, major = major)
        data = serializers.serialize("json",noticedetail,fields = ('num','title','writer','content','file_url','date','img'))   
        temp = json.loads(data)
        if(temp[0]['fields']['file_url'] != None):
            temp[0]['fields']['file_url'] = temp[0]['fields']['file_url'].split()
        data = json.dumps(temp, indent=2, ensure_ascii=False)
        return HttpResponse(content=data)
    """
