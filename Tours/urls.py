from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(openapi.Info(
    title='Документация для проекта "Туристические путешествия"',
    description='Сайт "Туристические путешествия"',
    default_version='v1'
), public=True)


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('Packets.urls')),
    path('api/v1/', include('Reviews.urls')),
]


"""Подключение media и static"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
