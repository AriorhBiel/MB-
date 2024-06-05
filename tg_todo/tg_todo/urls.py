from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from todo.drf_views import UserViewSet, RecordViewSet, DateViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'record', RecordViewSet)
router.register(r'date', DateViewSet)

urlpatterns = [
    path('', include('todo.urls')),
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(), name='swagger_ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]

urlpatterns += router.urls
