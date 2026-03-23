from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from department.models import Department
from teacher.models import Teacher

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})

def add_subject(request):
    departments = Department.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        description = request.POST.get('description')

        department = Department.objects.get(id=department_id)
        teacher = None
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)

        Subject.objects.create(
            name=name,
            code=code,
            department=department,
            teacher=teacher,
            description=description
        )
        return redirect('subject_list')

    return render(request, 'subjects/add-subject.html', {
        'departments': departments,
        'teachers': teachers
    })

def subject_details(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subjects/subject-details.html', {'subject': subject})

def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    departments = Department.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')

        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')

        subject.department = Department.objects.get(id=department_id)

        if teacher_id:
            subject.teacher = Teacher.objects.get(id=teacher_id)
        else:
            subject.teacher = None

        subject.description = request.POST.get('description')
        subject.save()
        return redirect('subject_list')

    return render(request, 'subjects/edit-subject.html', {
        'subject': subject,
        'departments': departments,
        'teachers': teachers
    })

def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return redirect('subject_list')
