from django.contrib import admin
from .models import Project, Task
# Register your models here.
@admin.register(Project)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Task)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id','name','project')