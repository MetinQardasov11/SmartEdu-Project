from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    students = models.ManyToManyField(User, blank=True, null=True, related_name='courses_joined')
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d', default='courses/default_course_img.png')
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'