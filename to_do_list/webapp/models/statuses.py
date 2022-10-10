from django.db import models



class Statuses(models.Model):
    status = models.CharField(
        verbose_name='Статус задачи', 
        max_length=100
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f'{self.status}'