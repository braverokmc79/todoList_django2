from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView

def signup(request):
    if request.method == 'POST':
        # 회원가입 처리 로직
        form =UserCreationForm(request.POST)
        if( form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        # GET 요청 시 회원가입 폼을 보여줌
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})    



class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # 커스텀 로그인 템플릿 경로 지정
    redirect_authenticated_user = True  # 로그인한 사용자가 로그인 페이지에 접근할 때 리다이렉트 설정
    extra_context = {'title': '로그인'}  # 추가 컨텍스트 변수 설정  