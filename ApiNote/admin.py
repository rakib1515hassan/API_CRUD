from django.contrib import admin
from ApiNote.models import Teacher


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'salary', 'experience')