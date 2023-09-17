from django.urls import path
from payments.views import (
    CreateCheckoutSessionView,
    PaymentSuccessView,
    PaymentCancelView,
    stripe_webhook_view,
)


urlpatterns = [
    path(
        "create-checkout-session/",
        CreateCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/", PaymentSuccessView.as_view(), name="payment-success"),
    path("cancel/", PaymentCancelView.as_view(), name="payment-cancel"),
    path("webhook/", stripe_webhook_view, name="payment-webhook"),
]
