from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class SaveStripeInfo(APIView):
    def post(self,request):
        data = request.data
        email = data['email']
        payment_method_id = data['payment_method_id']
        course_fee=data['course_fee']

        # checking if customer already exist
        customer_data = stripe.Customer.list(email=email).data

        if len(customer_data)==0:
            # creating customer
            customer = stripe.Customer.create(email=email,payment_method=payment_method_id)
        else:
            customer = customer_data[0]

        stripe.PaymentIntent.create(
            customer=customer, 
            payment_method=payment_method_id,  
            currency='usd', 
            amount=course_fee,
            confirm=True
        )
        
        return Response(status=status.HTTP_200_OK, 
            data={
                'message': 'Success', 
                'data': {'customer_id': customer.id} 
            } 
        ) 

class StripePaymentView(APIView):
    def post(self,request):
        try:
            test_payment_intent = stripe.PaymentIntent.create(
            amount=1000, currency='pln', 
            payment_method_types=['card'],
            receipt_email='test@example.com')
            return Response(status=status.HTTP_200_OK, data=test_payment_intent)
        except :
            return Response(
                {'error':'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    



        
