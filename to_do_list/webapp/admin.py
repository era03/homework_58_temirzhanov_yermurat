from django.contrib import admin
from webapp.models import  Types, Statuses, Tasks



class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'task', 'description', 'status', 'created_at', 'updated_at')
    search_fields = ('task', 'created_at', 'updated_at', 'status')
    fields = ('task', 'description', 'status', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
  

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'status', 'created_at', 'updated_at')
    search_fields = ('status', 'created_at', 'updated_at')
    fields = ('status', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'created_at', 'updated_at')
    list_filter = ('id', 'type_name', 'created_at', 'updated_at')
    search_fields = ('type_name', 'created_at', 'updated_at')
    fields = ('type_name', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Tasks, TaskAdmin)
admin.site.register(Statuses, StatusAdmin)
admin.site.register(Types, TypeAdmin)