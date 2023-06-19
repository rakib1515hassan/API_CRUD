from django.contrib import admin
from app.models import Student


# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'gender', 'roll', 'email', 'waiver', 'description', 'date_of_birth', 'created_at' )

