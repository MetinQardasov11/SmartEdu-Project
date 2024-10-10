from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m/%d', default='courses/default_course_img.png')
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'