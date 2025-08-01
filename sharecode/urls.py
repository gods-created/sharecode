from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('django_prometheus.urls')),
    path('', include('web.urls', namespace='web')),
    path('api/', include('api.urls', namespace='api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
