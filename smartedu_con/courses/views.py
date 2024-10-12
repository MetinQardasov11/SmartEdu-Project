from django.shortcuts import render
from .models import Course

# Create your views here.

def course_list(request):
    courses = Course.objects.all().order_by('-date')
    
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)

def course_detail(request, category_slug, category_id):
    course = Course.objects.get(id=category_id, category__slug=category_slug)
    
    context = {
        'course': course
    }
    return render(request, 'course_detail.html', context)

