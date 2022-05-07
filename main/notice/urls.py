from notice import views
from django.urls import path 

urlpatterns = [
    path('',views.NoticeList.as_view() ),
    #path('<int:major>/notice/<int:noticenum>', views.NoticeDetail.as_view())
    path('<int:noticenum>', views.NoticeDetail.as_view()),
    #path('<int:major>/notice/<str:search>',views.NoticeSearch.as_view())
    path('search', views.NoticeSearch.as_view(), name='keyword')
]
