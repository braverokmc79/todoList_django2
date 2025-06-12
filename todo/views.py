from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse ,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# ✅ 포인트:
# 🔖 LoginRequiredMixin: 로그인하지 않으면 접근 불가.
# 🔖 UserIsOwnerMixin: 다른 사람 데이터 접근 제한.
# form_valid: 생성 시 작성자를 현재 로그인 유저로 설정.    

# 권한 체크 Mixin
class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        todo = self.get_object()
        return todo.author == self.request.user    
       

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"
    paginate_by = 5

    def get_queryset(self):
        queryset = Todo.objects.filter(author=self.request.user)

        # 검색
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(name__icontains=query)

        # 완료 여부 필터
        complete_filter = self.request.GET.get("complete")
        if complete_filter == "complete":
            queryset = queryset.filter(complete=True)
        elif complete_filter == "incomplete":
            queryset = queryset.filter(complete=False)

        # 정렬
        sort = self.request.GET.get("sort")
        if sort == "exp":
            queryset = queryset.order_by("-exp")
        elif sort == "complete_date":
            queryset = queryset.order_by("-completed_at")
        else:  # 기본값: 생성일 최신순
            queryset = queryset.order_by("-created_at")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        context["complete_filter"] = self.request.GET.get("complete", "")
        context["sort"] = self.request.GET.get("sort", "")
        return context
  
    
    
class TodoCreateView(LoginRequiredMixin , CreateView):
     model = Todo
     fields = ['name', 'description', 'complete', 'exp']  # 사용할 필드
     template_name = "todo/todo_create.html"  # 사용할 템플릿 경로
     success_url = reverse_lazy("todo:todo_list")  # 성공 후 리다이렉트할 URL
    
     def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
     

    

    
    
class TodoDetailView(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
     model = Todo
     template_name = "todo/todo_detail.html"
     context_object_name = "todo" # 템플릿에서 사용할 변수명
     
    
    
class TodoUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
     model = Todo
     fields = ['name', 'description', 'complete', 'exp']  # 사용할 필드
     template_name = "todo/todo_update.html"  # 사용할 템플릿 경로
     success_url= reverse_lazy("todo:todo_list") # 성공 후 리다이렉트할 URL     
    
    
    
class TodoDeleteView(LoginRequiredMixin, UserIsOwnerMixin,DeleteView):
    model = Todo
    success_url = reverse_lazy("todo:todo_list")   # 삭제 후 리다이렉트할 URL     
                
                
                