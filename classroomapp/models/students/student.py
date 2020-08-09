from django.db import models
from classroomapp.models import Cohort, Exercise


class Student(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    slack = models.CharField(max_length=50)
    exercises = models.ManyToManyField(Exercise)
    cohort = models.ForeignKey(
        Cohort,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.first} {self.last}"
