from django.contrib import admin
from django.urls import path, include
from home_auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.dashboard, name='dashboard'),

    path('student/', include('student.urls')),
    path('authentication/', include('home_auth.urls')),
    path('teachers/', include('teacher.urls')),
    path('departments/', include('department.urls')),
    path('subjects/', include('subject.urls')),
    path('timetable/', include('timetable.urls')),
    path('holiday/', include('holiday.urls')),
    path('exam/', include('exam.urls')),
]