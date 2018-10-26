from django.conf.urls import url
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('blog/add/', views.add, name='add'),
    path('blog/edit/<int:entry_id>/', views.edit, name='edit'),
]