from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signup, name='signup'),    
    path('login/', views.CustomLoginView.as_view(), name='login'),  # 커스텀 로그인 뷰 등록
]