from flask import current_app
import stripe

stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

def create_payment(amount, currency, source):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method=source,
            confirmation_method='manual',
            confirm=True,
        )
        return payment_intent
    except stripe.error.CardError as e:
        return {'error': str(e)}, 400
    except Exception as e:
        return {'error': 'Payment processing error: ' + str(e)}, 500

def verify_payment(payment_intent_id):
    try:
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return payment_intent
    except Exception as e:
        return {'error': 'Payment verification error: ' + str(e)}, 500