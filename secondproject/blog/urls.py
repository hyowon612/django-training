from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
