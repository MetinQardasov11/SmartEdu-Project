from django.urls import path
from .views import *

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='teachers'),
]