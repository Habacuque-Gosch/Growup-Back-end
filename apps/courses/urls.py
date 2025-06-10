from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'modules', ModuleViewSet, basename='modules')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'contents', ContentViewSet, basename='contents')
# router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]