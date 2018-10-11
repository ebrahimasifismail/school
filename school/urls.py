from django.contrib import admin
from django.urls import path, include

from school.views import IndexList, StudentList
from . import views

app_name = 'school'
urlpatterns = [
    path('', IndexList.as_view(), name='index'),
    path('class/<int:pk>/', views.StudentList.as_view(), name='classes'),
    path('class/<int:pk>/student/<int:student_pk>/', views.student_detail, name='student'),      
]