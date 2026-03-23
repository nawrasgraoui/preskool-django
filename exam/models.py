from django.db import models
from subject.models import Subject


class Exam(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateField()
    exam_time = models.TimeField()
    room = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title