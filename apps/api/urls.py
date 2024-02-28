# Author:Yu WeiJie
# System: Mac
from django.urls import path, re_path
from apps.api import views

urlpatterns = [
    path('home/', views.home),
    # 访问连接: http://127.0.0.1:8000/api/login/yu/
    path('login/<str:role>/', views.login, name="v1"),
    # 访问连接: http://127.0.0.1:8000/api/auth/666/yu/
    re_path(r'auth/(\d+)/(\w+)/', views.auth, name="v2")
]

