from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    # path('courses/', CoursesAPIView.as_view(), name='courses'),
    # path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    # path('courses/<int:course_pk>/reviews/', ReviewsAPIView.as_view(), name='course_reviews'),
    # path('courses/<int:course_pk>/reviews/<int:review_pk>', ReviewAPIView.as_view(), name='course_review'),
    # path('reviews/', ReviewsAPIView.as_view(), name='reviews'),
    # path('reviews/<int:review_pk>', ReviewAPIView.as_view(), name='review'),
]