from django.contrib import admin
from django.urls import path
from webapp.views.base import IndexView
from webapp.views.tasks import TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView




urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', IndexView.as_view()),
    path('add/', TaskCreateView.as_view(), name='create_task'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='detail_task')
]