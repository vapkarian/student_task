from django.db import models
from django_history.models import HistoricalRecords

class Group(models.Model):
    title = models.CharField(max_length=10)
    praepostor = models.ForeignKey('Student', related_name="subgroup",
                                   blank=True, null=True)
    history = HistoricalRecords()
    def __unicode__(self):
        return self.title

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    birthday = models.DateField(blank=True, null=True)
    student_number = models.CharField(max_length=10, blank=True)
    group = models.ForeignKey('Group', related_name="students")
    history = HistoricalRecords()
    def __unicode__(self):
        return self.full_name
