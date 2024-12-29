from django.urls import path
from .views.views import *

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('reviews/', ReviewsAPIView.as_view(), name='reviews'),
    path('reviews/<int:pk>', ReviewAPIView.as_view(), name='review'),
]