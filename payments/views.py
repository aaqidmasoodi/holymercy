import stripe
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"


class PaymentCancelView(TemplateView):
    template_name = "payments/cancel.html"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000/payments"
        checkout_session = ""
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "inr",
                            "unit_amount": 1000,
                            "product_data": {
                                "name": "holy mercy premium",
                                # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        "quantity": 1,
                    },
                ],
                metadata={"product_id": 2},
                mode="payment",
                success_url=YOUR_DOMAIN + "/success/",
                cancel_url=YOUR_DOMAIN + "/cancel/",
            )
        except stripe.error.StripeError as e:
            print("Stripe Error:", e)
        except Exception as e:
            print("ERROR!!!!")
            return str(e)
        return redirect(checkout_session.url, code=303)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event["data"]["object"]["id"],
            expand=["line_items"],
        )

        line_items = session.line_items
        # Fulfill the purchase...
        print("Fulling the order....")

    # Passed signature verification
    return HttpResponse(status=200)
