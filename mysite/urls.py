from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home_view, gallery_view, premium_features_view, books_view
from accounts.views import login_view, signup_view
from payments.views import CreateCheckoutSessionView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("premium/", premium_features_view, name="premium-features"),
    path("books/", books_view, name="books"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("gallery/", gallery_view, name="gallery"),
    path("payments/", include("payments.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
