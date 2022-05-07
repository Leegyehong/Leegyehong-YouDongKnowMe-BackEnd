from notice import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<str:majorname>/notice', views.NoticeList.as_view()),
    path('notice/', views.NoticeList.as_view()),
    #path('<str:major>/notice/<int:noticenum>', views.NoticeDetail.as_view())
    path('notice/<int:noticenum>', views.NoticeDetail.as_view()),
    path('apikey/', include('apikey.urls'), name='apikey')
]
