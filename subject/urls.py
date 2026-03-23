from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('add/', views.add_subject, name='add_subject'),
    path('<int:pk>/', views.subject_details, name='subject_details'),
    path('edit/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('delete/<int:pk>/', views.delete_subject, name='delete_subject'),
]