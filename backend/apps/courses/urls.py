from django.urls import path
from .views.views import *

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('reviews/', ReviewAPIView.as_view(), name='reviews'),
]