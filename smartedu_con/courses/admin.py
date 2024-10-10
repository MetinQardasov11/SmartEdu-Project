from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'available')
    list_filter = ('available', 'date')
    search_fields = ('name', 'description')