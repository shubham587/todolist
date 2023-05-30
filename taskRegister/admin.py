from django.contrib import admin
from .models import TaskList
# Register your models here.
@admin.register(TaskList)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')