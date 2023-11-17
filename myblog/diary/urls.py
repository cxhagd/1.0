# diary/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('entries/', views.diary_list, name='diary_list'),
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # 设置主页为登录页面
    path('register/', views.register, name='register'),  # 添加这行
    path('accounts/', include('django.contrib.auth.urls')),  # 用于认证系统的 URL
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='diary/logout.html'), name='logout'),
    path('entry/<int:pk>/', views.diary_detail, name='diary_detail'),
    path('entry/new/', views.diary_create, name='diary_create'),
    path('calendar/<int:year>/<int:month>/', views.get_calendar, name='calendar'),
    path('entry/<int:year>/<int:month>/<int:day>/', views.diary_detail, name='diary_detail'),
    path('calendar/<int:year>/<int:month>/', views.get_calendar, name='calendar'),
    path('my-view/', views.my_view, name='my_view'),
    # 其他 URL 配置...
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


