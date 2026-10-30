from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Admin password reset (enables "Forgotten your password?" link on admin login)
    path("admin/password_reset/", auth_views.PasswordResetView.as_view(), name="admin_password_reset"),
    path("admin/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("admin/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("admin/reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("", include("portfolio.urls")),
]

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as media_serve

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [path('media/<path:path>', media_serve, {'document_root': settings.MEDIA_ROOT})]
