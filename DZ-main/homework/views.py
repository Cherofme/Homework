from django.shortcuts import render
from .models import Project, Task
# Create your views here

def home(request):
    projects = Project.objects.all()
    context ={'projects': projects}
    return render(request,'index.html',context)

def task(request,project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'task.html', {'project': project, 'tasks': tasks})