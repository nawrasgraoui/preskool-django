from django.shortcuts import render, redirect, get_object_or_404
from .models import Exam
from subject.models import Subject


def exam_list(request):
    exams = Exam.objects.select_related('subject').all().order_by('exam_date', 'exam_time')
    return render(request, 'exams/exams.html', {'exams': exams})


def add_exam(request):
    subjects = Subject.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        subject_id = request.POST.get('subject')
        exam_date = request.POST.get('exam_date')
        exam_time = request.POST.get('exam_time')
        room = request.POST.get('room')
        description = request.POST.get('description')

        subject = Subject.objects.get(id=subject_id)

        Exam.objects.create(
            title=title,
            subject=subject,
            exam_date=exam_date,
            exam_time=exam_time,
            room=room,
            description=description
        )
        return redirect('exam_list')

    return render(request, 'exams/add-exam.html', {'subjects': subjects})


def edit_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    subjects = Subject.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        subject_id = request.POST.get('subject')
        exam_date = request.POST.get('exam_date')
        exam_time = request.POST.get('exam_time')
        room = request.POST.get('room')
        description = request.POST.get('description')

        exam.title = title
        exam.subject = Subject.objects.get(id=subject_id)
        exam.exam_date = exam_date
        exam.exam_time = exam_time
        exam.room = room
        exam.description = description
        exam.save()

        return redirect('exam_list')

    return render(request, 'exams/edit-exam.html', {
        'exam': exam,
        'subjects': subjects
    })


def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')

    return redirect('exam_list')
