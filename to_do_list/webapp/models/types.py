from django.db import models



class Types(models.Model):
    type_name = models.CharField(
        verbose_name='Тип задачи', 
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
        return f'{self.type_name}'