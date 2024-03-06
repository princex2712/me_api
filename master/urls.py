from django.urls import path
from .views import *

urlpatterns = [
    path('',taskListAPI,name='taskListAPI'),
]
