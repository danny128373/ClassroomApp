from django.db import models


class Cohort(models.Model):
    name = models.CharField(max_length=50)
