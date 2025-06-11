from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'complete', 'exp', 'completed_at', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('complete', 'created_at')
    
    
admin.site.register(Todo, TodoAdmin)
