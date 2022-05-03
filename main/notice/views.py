from dataclasses import fields
from logging import exception
from multiprocessing.sharedctypes import Value
from re import L
from django.http import HttpResponse,JsonResponse,Http404
from django.views import View
from .models import Noti
from django.core import serializers
from http import HTTPStatus
import json

# Create your views here.


class NoticeList(View):
    """
    def get(self, requset, major):
         try:
            notice = Noti.objects.using('crawled_data').filter(major = major).order_by('-num')
            if notice.count() == 0:
                raise Exception()
            else:
                data = serializers.serialize("json", list(
                    notice), fields=('num', 'title','date', 'writer'))
                temp = json.loads(data)
                datalist = []  
                for i in range(len(temp)):
                    datalist.append(temp[i]['fields'])
                data = json.dumps(datalist, indent=2, ensure_ascii=False)
                return HttpResponse(data, content_type="text/json-comment-filtered")
        except Exception as e:
            return JsonResponse({'message':'error'},status=HTTPStatus.BAD_REQUEST)
    """

    def get(self, requset):
        try:
            notice = Noti.objects.using('crawled_data').all().order_by('-num')
            if notice.count() == 0:
                raise Exception()
            else:
                data = serializers.serialize("json", list(
                    notice), fields=('num', 'title','date', 'writer'))
                temp = json.loads(data)
                datalist = []  
                for i in range(len(temp)):
                    datalist.append(temp[i]['fields'])
                data = json.dumps(datalist, indent=2, ensure_ascii=False)
                return HttpResponse(data, content_type="application/json")
        except Exception as e:
            return JsonResponse({'message':'error'},status=HTTPStatus.BAD_REQUEST)
            #raise JS('게시글을 찾을 수 없습니다 다시 요청해주세요!')


class NoticeDetail(View):

    def get(self, requset, noticenum):
        try:
            noticedetail = Noti.objects.using('crawled_data').filter(num = noticenum).order_by('-num')
            data = serializers.serialize("json", noticedetail, fields=(
                'num', 'title', 'writer', 'content', 'file_url', 'date', 'img_url'))
            
            temp = json.loads(data)
            
            for i in temp[0]['fields']:
                if(temp[0]['fields'][i] == None or temp[0]['fields'][i].replace(" ", "") == ""):
                    temp[0]['fields'][i] = ""
                
            if(temp[0]['fields']['file_url'] != ""):
                temp[0]['fields']['file_url'] = temp[0]['fields']['file_url'].split()
            if(temp[0]['fields']['img_url'] != ""):
                temp[0]['fields']['img_url'] = temp[0]['fields']['img_url'].split()
                
            data = json.dumps(temp[0]['fields'], indent=2, ensure_ascii=False)
            return HttpResponse(content=data)
        
        except Exception as e:
            return JsonResponse({'message':'error'},status=HTTPStatus.BAD_REQUEST)
   
"""
   class NoticeDetail(View):
    
    def get(self, requset, noticenum, major):
        try:
            noticedetail = Noti.objects.using('crawled_data').filter(num = noticenum, major = major).order_by('-num')
            data = serializers.serialize("json", noticedetail, fields=(
                'num', 'title', 'writer', 'content', 'file_url', 'date', 'img_url'))
            temp = json.loads(data)
            for i in temp[0]['fields']:
                if(temp[0]['fields'][i] == None or temp[0]['fields'][i].replace(" ", "") == ""):
                    temp[0]['fields'][i] = ""
                
            if(temp[0]['fields']['file_url'] != ""):
                temp[0]['fields']['file_url'] = temp[0]['fields']['file_url'].split()
            if(temp[0]['fields']['img_url'] != ""):
                temp[0]['fields']['img_url'] = temp[0]['fields']['img_url'].split()
                
            data = json.dumps(temp, indent=2, ensure_ascii=False)
            return HttpResponse(content=data)
        
        except Exception as e:
            return JsonResponse({'message':'error'},status=HTTPStatus.BAD_REQUEST)
"""

class NoticeSearch(View):
    def get(self, request):
        try:
            keyword = request.GET['keyword']
            print(keyword)
            searchList = Noti.objects.filter(
                title__contains=keyword).order_by('-num')
            if searchList.count() == 0:
                raise Exception()
            else:
                data = serializers.serialize("json", list(
                    searchList), fields=('num', 'title', 'date', 'writer'))
                temp = json.loads(data)
                datalist = []
                for i in range(len(temp)):
                    datalist.append(temp[i]['fields'])
                data = json.dumps(datalist, indent=2, ensure_ascii=False)
                return HttpResponse(data, content_type="application/json")
        except Exception as e:
            return JsonResponse({'message': 'error'}, status=HTTPStatus.BAD_REQUEST)
    """
    def get(self, requset, search, major):
        try :
            searchList = Noti.objects.using('crawled_data').filter(title__contains = search, major = major).order_by('-num')
            if searchList.count() == 0:
                raise Exception()
            else:
                data = serializers.serialize("json", list(
                    searchList), fields=('num', 'title','date', 'writer'))
                temp = json.loads(data)
                datalist = []  
                for i in range(len(temp)):
                    datalist.append(temp[i]['fields'])
                data = json.dumps(datalist, indent=2, ensure_ascii=False)
                return HttpResponse(data, content_type="application/json")
        except Exception as e:
            return JsonResponse({'message':'error'},status=HTTPStatus.BAD_REQUEST)
    """
