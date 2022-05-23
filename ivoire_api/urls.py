"""
    ivoire_api URL Configuration
"""

from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView






urlpatterns = [
    path(f'{settings.ADMIN_PAGE_URL}/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include('core.urls')),
    path('api/v1/news/', include('news.v1.urls')),
    path('api/v1/receipes/', include('receipes.v1.urls')),

    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

urlpatterns += static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)
