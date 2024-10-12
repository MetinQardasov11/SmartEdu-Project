from django.contrib import admin
from .models import Course, Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'category')
    list_filter = ('available', 'date')
    search_fields = ('name', 'description')
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}