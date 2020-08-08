from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from classroomapp.models import Cohort


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    slack = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    cohort = models.ForeignKey(
        Cohort,
        null=True,
        blank=True,
        on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_instructor(sender, instance, created, **kwargs):
    if created:
        Instructor.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_instructor(sender, instance, **kwargs):
    instance.instructor.save()
