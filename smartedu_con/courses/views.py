from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Tag

# Create your views here.

# def course_list(request):
    # courses = Course.objects.all().order_by('-date')
    # categories = Category.objects.all()
    # tags = Tag.objects.all()
    
    # context = {
    #     'courses': courses,
    #     'categories' : categories,
    #     'tags' : tags
    # }
    # return render(request, 'courses.html', context)

# def category_list(request, category_slug):
#     courses = Course.objects.all().filter(category__slug=category_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
    
#     context = {
#         'courses': courses,
#         'categories' : categories,
#         'tags' : tags
#     }
#     return render(request, 'courses.html', context)


# def tag_list(request, tag_slug):
#     courses = Course.objects.all().filter(tags__slug=tag_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
    
#     context = {
#         'courses': courses,
#         'categories' : categories,
#         'tags' : tags
#     }
#     return render(request, 'courses.html', context)


def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=category_page, available=True)
            
    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(tags=tag_page, available=True)
    
    else:
        courses = Course.objects.all().order_by('-date')
        
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


def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses': courses,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'courses.html', context)