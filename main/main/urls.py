from notice import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:majorname>/notice', views.NoticeList.as_view()),
    path('<str:major>/notice/<int:noticenum>', views.NoticeDetail.as_view())
]