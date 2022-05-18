from notice import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:major>/notice', views.NoticeList.as_view()),
    path('notice/', include('notice.urls')),
    path('schedule/<int:month>',views.scheduleList.as_view())
]
