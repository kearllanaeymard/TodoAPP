from django.urls import path
from . import views

app_name = 'todolist'

urlpatterns=[
    path('login/', views.loginview, name='loginview'),
]