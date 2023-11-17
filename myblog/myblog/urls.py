# myblog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),  # 指向您的应用的 URL 配置

]
