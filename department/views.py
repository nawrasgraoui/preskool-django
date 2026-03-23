from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from teacher.models import Teacher

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

def add_department(request):
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        department_head_id = request.POST.get('department_head')

        department_head = None
        if department_head_id:
            department_head = Teacher.objects.get(id=department_head_id)

        Department.objects.create(
            name=name,
            description=description,
            department_head=department_head
        )
        return redirect('department_list')

    return render(request, 'departments/add-department.html', {'teachers': teachers})

def department_details(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/department-details.html', {'department': department})

def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')

        department_head_id = request.POST.get('department_head')
        if department_head_id:
            department.department_head = Teacher.objects.get(id=department_head_id)
        else:
            department.department_head = None

        department.save()
        return redirect('department_list')

    return render(request, 'departments/edit-department.html', {
        'department': department,
        'teachers': teachers
    })

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return redirect('department_list')
