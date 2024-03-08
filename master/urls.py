from django.urls import path
from .views import *

urlpatterns = [
    path('',taskListAPI,name='taskListAPI'),
    path('task/<int:task_id>',tastDetailAPI,name='tastDetailAPI'),
]
