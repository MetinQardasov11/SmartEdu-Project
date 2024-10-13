from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('', course_list, name='courses'),
    path('<slug:category_slug>/<int:category_id>', course_detail, name='course_detail'),
    path('categories/<slug:category_slug>/', category_list, name='course_by_category'),
    path('tags/<slug:tag_slug>/', tag_list, name='course_by_tag'),
    
]