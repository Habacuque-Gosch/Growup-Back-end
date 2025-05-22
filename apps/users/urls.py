from django.urls import path
from .views import *
from django.urls import path, include
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomEmailTokenObtainPairView.as_view(), name='login'),
    path('', include(router.urls)),
]
