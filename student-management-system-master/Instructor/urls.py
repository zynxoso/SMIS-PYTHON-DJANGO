from django.urls import path

from . import views

urlpatterns = [
    path('', views.instructor_index, name='instructor_index'),
    path('<int:id>', views.view_instructor, name='view_instructor'),
    path('instructor_add/', views.  instructor_add, name='instructor_add'),
    path('instructor_edit/<int:id>/', views.instructor_edit, name='instructor_edit'),
    path('instructor_delete/<int:id>/', views.instructor_delete, name='instructor_delete'),
]

76