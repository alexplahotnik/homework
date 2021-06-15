from django.db import models
from django.utils import timezone


class Homework(models.Model):
    text = models.CharField(max_length=40)
    deadline = models.DurationField()
    created_date = models.DateTimeField(default=timezone.now)


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class HomeworkResult(models.Model):
    author = models.ManyToManyField(Student)
    homework = models.ManyToManyField(Homework)
    solution = models.CharField(max_length=20)
