import React from 'react';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from '@stripe/stripe-js';
import Card from './Card'
import CheckoutForm from './CheckoutForm';

export class Cart extends React.Component {

  constructor(props) {
    super(props);    
    this.state = {
      data: null,
      isCheckedoutInitiated: false,
    };
    const stripePromise = loadStripe("pk_test_T9fxZn2iOenlAzEV87I8wvrK");
  }

	 checkout() {
	  fetch("http://localhost:4242/create-payment-intent")
       .then(response => response.json()
       .then(
        data => {this.setState({data: data["secret"]})})
       )
       this.setState({isCheckedoutInitiated: true})
   }

   back() {
    this.setState({isCheckedoutInitiated: false})
   }
 

render() {
  if(!this.state.isCheckedoutInitiated)
   {
    return(
        <div>     
                 <h1>Your Cart </h1>
                 <h2>Mutual Funds</h2>
                 <p> S&P 500 Index (SPX)</p>
                 <p> USD 2,972.37 </p>
                 <button onClick={() => this.checkout()}> Buy now </button>      
        </div>
    );
   }
   else
   {
    return (
      <div>
            <div>
              <h1>Enter Card Details</h1>
              <button onClick={() => this.back()}> BACK </button>
              <br/>
              <br/>
            </div>

            <div>
                <Card secret={this.state.data}/>
            </div>
      </div>
    );
   }
  }
}
