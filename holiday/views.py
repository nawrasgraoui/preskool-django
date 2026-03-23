from django.shortcuts import render, redirect, get_object_or_404
from .models import Holiday


def holiday_list(request):
    holidays = Holiday.objects.all().order_by('date')
    return render(request, 'holidays/holidays.html', {'holidays': holidays})


def add_holiday(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')

        Holiday.objects.create(
            title=title,
            date=date,
            description=description
        )
        return redirect('holiday_list')

    return render(request, 'holidays/add-holiday.html')


def edit_holiday(request, holiday_id):
    holiday = get_object_or_404(Holiday, id=holiday_id)

    if request.method == 'POST':
        holiday.title = request.POST.get('title')
        holiday.date = request.POST.get('date')
        holiday.description = request.POST.get('description')
        holiday.save()
        return redirect('holiday_list')

    return render(request, 'holidays/edit-holiday.html', {'holiday': holiday})


def delete_holiday(request, holiday_id):
    holiday = get_object_or_404(Holiday, id=holiday_id)

    if request.method == 'POST':
        holiday.delete()
        return redirect('holiday_list')

    return redirect('holiday_list')