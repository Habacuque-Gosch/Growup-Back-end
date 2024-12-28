from django.urls import path
from .views.views import *

urlpatterns = [
    path('', get_all_users),
    path('users/<str:name>', get_by_name),
    path('manager/', user_manager),
]