from django import forms
from .models import Todo
from django.core.exceptions import ValidationError

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        """
        ModelForm 유효성 검사:
        - 완료 상태일 경우 completed_at은 있어야 함
        - 완료 상태가 아닐 경우 completed_at은 없어서는 안 됨
        """
        cleaned_data = super().clean()
        complete = cleaned_data.get("complete")
        completed_at = cleaned_data.get("completed_at")

        if complete and completed_at is None:
            raise ValidationError("완료된 항목은 완료일시(completed_at)가 필요합니다.")
        if not complete and completed_at is not None:
            raise ValidationError("완료되지 않은 항목은 완료일시(completed_at)를 가질 수 없습니다.")



