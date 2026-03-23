from django.db import models
from teacher.models import Teacher

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department_head = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments'
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
