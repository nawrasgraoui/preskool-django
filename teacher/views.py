from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        address = request.POST.get('address')

        Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            teacher_id=teacher_id,
            email=email,
            phone=phone,
            qualification=qualification,
            address=address
        )
        return redirect('teacher_list')

    return render(request, 'teachers/add-teacher.html')

def teacher_details(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})

def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.teacher_id = request.POST.get('teacher_id')
        teacher.email = request.POST.get('email')
        teacher.phone = request.POST.get('phone')
        teacher.qualification = request.POST.get('qualification')
        teacher.address = request.POST.get('address')
        teacher.save()
        return redirect('teacher_list')

    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher})

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return redirect('teacher_list')