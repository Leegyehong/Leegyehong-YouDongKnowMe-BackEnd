from notice import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:major>/notice', views.NoticeList.as_view()),
    path('notice/', views.NoticeList.as_view()),
    #path('<int:major>/notice/<int:noticenum>', views.NoticeDetail.as_view())
    path('notice/<int:noticenum>', views.NoticeDetail.as_view()),
    #path('<int:major>/notice/<str:search>',views.NoticeSearch.as_view())
    path('notice/search', views.NoticeSearch.as_view(), name='keyword')
]
