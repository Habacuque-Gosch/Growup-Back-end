from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.courses.urls import router




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.courses.urls')),
    path('api/v2/', include(router.urls)),
    path('auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
