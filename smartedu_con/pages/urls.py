from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('teachers/', teachers, name='teachers'),
    path('contact/', contact, name='contact'),
]