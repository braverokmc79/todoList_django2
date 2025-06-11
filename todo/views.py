from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo



class TodoListView(ListView):
    model =Todo
    template_name = "todo/todo_list.html"  # 사용할 템플릿 경로
    context_object_name = "todos"  # 템플릿에서 사용할 객체 이름
    ordering = ['-created_at']  # 생성 시각 기준으로 내림차순 정렬
   
    
class TodoCreateView(CreateView):
     model = Todo
     fields = ['name', 'description', 'complete', 'exp']  # 사용할 필드
     template_name = "todo/todo_form.html"  # 사용할 템플릿 경로
     success_url = "/todo/"  # 성공 후 리다이렉트할 URL
    
    
class TodoDetailView(DetailView):
     model = Todo
     template_name = "todo/todo_detail.html"
    
    
class TodoUpdateView(UpdateView):
     model = Todo
     fields = ['name', 'description', 'complete', 'exp']  # 사용할 필드
     template_name = "todo/todo_form.html"  # 사용할 템플릿 경로
     success_url = "/todo/"  # 성공 후 리다이렉트할 URL     
    
    
    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = "/todo/"
                