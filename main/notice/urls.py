from notice import views
from django.urls import path 

urlpatterns = [
    path('<int:major>',views.NoticeList.as_view() ),
    path('<int:major>/<int:noticenum>', views.NoticeDetail.as_view()),
    path('<int:major>/search', views.NoticeSearch.as_view(), name='keyword')
]
