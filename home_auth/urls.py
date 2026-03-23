from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/', views.reset_password_view, name='reset-password'),
]
