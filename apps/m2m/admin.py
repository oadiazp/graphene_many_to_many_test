from django.contrib import admin

from apps.m2m.models import Student, Group


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
