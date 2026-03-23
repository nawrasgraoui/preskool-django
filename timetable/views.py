from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeTable
from subject.models import Subject
from teacher.models import Teacher

def timetable_list(request):
    timetables = TimeTable.objects.all().order_by('day', 'start_time')
    return render(request, 'timetable/time-table.html', {'timetables': timetables})

def add_timetable(request):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        teacher_id = request.POST.get('teacher')
        day = request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        room = request.POST.get('room')
        description = request.POST.get('description')

        subject = Subject.objects.get(id=subject_id)
        teacher = None
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)

        TimeTable.objects.create(
            subject=subject,
            teacher=teacher,
            day=day,
            start_time=start_time,
            end_time=end_time,
            room=room,
            description=description
        )
        return redirect('timetable_list')

    return render(request, 'timetable/add-time-table.html', {
        'subjects': subjects,
        'teachers': teachers
    })

def timetable_details(request, pk):
    timetable = get_object_or_404(TimeTable, pk=pk)
    return render(request, 'timetable/time-table-details.html', {'timetable': timetable})

def edit_timetable(request, pk):
    timetable = get_object_or_404(TimeTable, pk=pk)
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        timetable.subject = Subject.objects.get(id=request.POST.get('subject'))

        teacher_id = request.POST.get('teacher')
        if teacher_id:
            timetable.teacher = Teacher.objects.get(id=teacher_id)
        else:
            timetable.teacher = None

        timetable.day = request.POST.get('day')
        timetable.start_time = request.POST.get('start_time')
        timetable.end_time = request.POST.get('end_time')
        timetable.room = request.POST.get('room')
        timetable.description = request.POST.get('description')
        timetable.save()

        return redirect('timetable_list')

    return render(request, 'timetable/edit-time-table.html', {
        'timetable': timetable,
        'subjects': subjects,
        'teachers': teachers
    })

def delete_timetable(request, pk):
    timetable = get_object_or_404(TimeTable, pk=pk)
    if request.method == 'POST':
        timetable.delete()
        return redirect('timetable_list')
    return redirect('timetable_list')

def visual_timetabling(request):
    return render(request, 'timetable/visual-timetabling.html')