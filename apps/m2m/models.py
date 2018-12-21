from django.db import models
from model_utils.models import TimeStampedModel


class Student(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(TimeStampedModel):
    name = models.CharField(max_length=100)

    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
