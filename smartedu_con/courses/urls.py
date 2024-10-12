from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('', course_list, name='courses'),
    path('<slug:category_slug>/<int:category_id>', course_detail, name='course_detail'),
]