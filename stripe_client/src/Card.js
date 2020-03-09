import React from 'react';
import ReactDOM from 'react-dom';
import CheckoutForm from './CheckoutForm';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe('pk_test_T9fxZn2iOenlAzEV87I8wvrK');

export default function Card(props) {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm secret={props.secret} />
    </Elements>
  );
};