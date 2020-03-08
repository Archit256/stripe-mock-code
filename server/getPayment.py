import stripe
import json
import os
import re
import urllib.parse
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)

CORS(app)

endpoint_secret='whsec_hYLiguc1vTf0vOyaLecTvcGKDm1J07it'

# Setup Stripe python client library
#stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
#stripe.api_version = os.getenv('STRIPE_API_VERSION')


@app.route('/', methods=['GET'])
def index():
    # Display checkout page
    return "Payment Server"


@app.route('/checkout', methods=['GET'])
def get_checkout_page():
    # Display checkout page
    return "Checkout"


@app.route('/create-payment-intent', methods=['POST', 'GET'])
def create_payment():
    #data = json.loads(request.data)
    stripe.api_key = 'sk_test_4U61mIixPZfWtT32raEDsScF'

    intent = stripe.PaymentIntent.create(
      amount=297237,
      currency='usd',
     # Verify your integration in this guide by including this parameter
      metadata={'integration_check': 'accept_a_payment'},
    )
    secret = {'secret': intent.client_secret}
    return secret


#webhook to receive payment responses
@app.route('/stripe-response', methods=['POST'])
def webhook_received():
    # You can use webhooks to receive information about asynchronous payment events.
    # For more about our webhook events check out https://stripe.com/docs/webhooks.
    request_data = json.loads(request.data)

    if endpoint_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=endpoint_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    if event_type == 'payment_intent.succeeded':
        print('💰 Payment received!')
        # Fulfill any orders, e-mail receipts, etc
        with open("orders.txt",'a',encoding = 'utf-8') as f:
            f.write(json.dumps(data_object)+"\n")
            f.write("\n")
        f.close()
        # To cancel the payment you will need to issue a Refund (https://stripe.com/docs/api/refunds)
    elif event_type == 'payment_intent.payment_failed':
        print('❌ Payment failed.')
    return jsonify({'status': 'success'})









