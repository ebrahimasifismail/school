from django.contrib import admin
from django.urls import path, include

from school.views import IndexList, StudentList
from . import views
from school.models import Classes, Student, Subject, OptionalSubject
app_name = 'school'
urlpatterns = [
    path('', IndexList.as_view(), name='index'),
    path('class/<int:pk>/', views.StudentList.as_view(), name='classes'),
    path('class/<int:pk>/student/<int:student_pk>/', views.student_detail.as_view(), name='student'),
    path('class/newclass/', views.ClassCreate.as_view(), name='newclass'),
    path('class/<int:pk>/editclass/', views.ClassUpdate.as_view(), name='editclasses'),
    path('class/<int:pk>/deleteclass/', views.ClassDeleteView.as_view(), name='deleteclasses'),
    path('class/newstudent/', views.StudentCreate.as_view(), name='newstudent'),
    path('class/<int:pk>/student/<int:student_pk>/edit', views.StudentUpdate.as_view(), name='editstudent'),
    path('class/<int:pk>/student/<int:student_pk>/deletestudent/', views.StudentDelete.as_view(), name='deletestudent'),      
    path('sub/', views.SubjectList.as_view(), name='sub'),
    path('subject/', views.SubjectStudentList.as_view(), name='subject')
]