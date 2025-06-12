from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include
from django.http import HttpResponseRedirect


def root_redirect(request):
    return HttpResponseRedirect('/todo/')


# 루트(/)에서 index.html 렌더링
def root_index_view(request):
    return render(request, 'index.html')  # templates/index.html

def signup_redirect_view(request):
    return HttpResponseRedirect('/accounts/signup/')

def login_redirect_view(request):
    return HttpResponseRedirect('/accounts/login/')


urlpatterns = [
    path('admin/', admin.site.urls),    
    path("todo/", include("todo.urls")),
    
    #path("", root_redirect),  # 루트 URL을 todo 앱의 index로 리다이렉트    
    path("", root_index_view),  # 루트에서 index.html 렌더링
    
     
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # 로그인, 로그아웃, 비밀번호 변경 등 기본 제공 URL 포함          
    path('signup/', signup_redirect_view), # /signup 으로 접근 시 /accounts/signup/으로 리다이렉트
    path('login/', login_redirect_view), # /login 으로 접근 시 /accounts/login/으로 리다이렉트
    
]
