from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView

# Create your views here.

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    paginate_by = 2
    
    