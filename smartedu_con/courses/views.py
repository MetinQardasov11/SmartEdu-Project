from django.shortcuts import render
from .models import Course, Category, Tag

# Create your views here.

def course_list(request):
    courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses': courses,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'courses.html', context)

def course_detail(request, category_slug, category_id):
    course = Course.objects.get(id=category_id, category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'course': course,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'course_detail.html', context)


def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses': courses,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'courses.html', context)


def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses': courses,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'courses.html', context)