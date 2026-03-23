from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
    path('add/', views.add_timetable, name='add_timetable'),
    path('<int:pk>/', views.timetable_details, name='timetable_details'),
    path('edit/<int:pk>/', views.edit_timetable, name='edit_timetable'),
    path('delete/<int:pk>/', views.delete_timetable, name='delete_timetable'),
    path('visual-timetabling/', views.visual_timetabling, name='visual_timetabling'),
]