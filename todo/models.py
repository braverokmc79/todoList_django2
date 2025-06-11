from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        """
        모델 유효성 검사:
        - 완료 상태일 경우 completed_at은 반드시 있어야 함
        - 완료 상태가 아닐 경우 completed_at은 없어야 함
        """
        if self.complete and self.completed_at is None:
            raise ValidationError("완료된 항목은 completed_at 날짜가 필요합니다.")
        if not self.complete and self.completed_at is not None:
            raise ValidationError("완료되지 않은 항목은 completed_at 날짜를 가질 수 없습니다.")

    def save(self, *args, **kwargs):
        # 상태 변화에 따라 completed_at 자동 설정
        #1. self.complete → True인 경우 (즉, "완료됨" 체크됨)
        #2. self.completed_at is None → 완료 시각이 아직 설정되지 않음
        #즉, "작업이 완료 상태로 표시되었는데, 완료 시각이 아직 없다면..."
        if self.complete and self.completed_at is None:
            self.completed_at = timezone.now()
        elif not self.complete:
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
