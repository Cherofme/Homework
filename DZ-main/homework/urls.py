from django.urls import path
from hm import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.task, name='project'),
]