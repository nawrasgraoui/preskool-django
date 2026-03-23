from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role')

        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True

        user.save()
        login(request, user)
        messages.success(request, 'Signup successful!')

        if user.is_admin:
            return redirect('admin_dashboard')
        elif user.is_teacher:
            return redirect('teacher_dashboard')
        else:
            return redirect('student_dashboard')

    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')

            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('student_dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return redirect('login')
    return render(request, 'authentication/student_dashboard.html')


@login_required
def teacher_dashboard(request):
    if not request.user.is_teacher:
        return redirect('login')
    return render(request, 'authentication/teacher_dashboard.html')


@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('login')
    return render(request, 'authentication/admin_dashboard.html')

def forgot_password_view(request):
    return render(request, 'authentication/forgot-password.html')

def reset_password_view(request, token):
    return render(request, 'authentication/reset_password.html')

