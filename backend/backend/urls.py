"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from backend import settings
from rest_framework_simplejwt.views import TokenRefreshView
from .serializer import MyTokenObtainPairView
from .views import Register

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理
    re_path(r'^register/', Register.as_view(), name="register"),  # 注册
    re_path(r'^login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # 登录token /登录
    re_path(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新token
    re_path(r'^api-auth/', include('rest_framework.urls')),  # drf视图
    re_path(r'^api/', include("api.urls")),  # api路由
    re_path(r'^tools/', include("tools.urls")),  # 工具路由
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 媒体资源路径
    re_path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})  # 静态资源路径
]
