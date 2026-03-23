from django.db import models


class Holiday(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
