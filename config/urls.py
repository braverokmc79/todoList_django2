from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include
from django.http import HttpResponseRedirect


def root_redirect(request):
    return HttpResponseRedirect('/todo/')


# 루트(/)에서 index.html 렌더링
def root_index_view(request):
    return render(request, 'index.html')  # templates/index.html


urlpatterns = [
    path('admin/', admin.site.urls),    
    path("todo/", include("todo.urls")),
    
    #path("", root_redirect),  # 루트 URL을 todo 앱의 index로 리다이렉트    
    path("", root_index_view),  # 루트에서 index.html 렌더링
]
