from django.contrib import admin
from models import Student, Group

class StudentInline(admin.TabularInline):
    model = Student

class GroupAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]

admin.site.register(Student)
admin.site.register(Group,GroupAdmin)
