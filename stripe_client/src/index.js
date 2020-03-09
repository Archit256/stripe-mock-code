import React from 'react';
import ReactDOM from 'react-dom';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';

import CheckoutForm from './CheckoutForm';
import {Cart} from './Cart';



ReactDOM.render(
	<Cart/>, 
	document.getElementById('root')
);