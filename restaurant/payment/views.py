import email

import braintree

from django.shortcuts import render, redirect, get_object_or_404

from orders.forms import OrderCreateForm
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail,EmailMultiAlternatives
from django.conf import settings
# import weasyprint
from io import BytesIO


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    orderName = request.session.get('orderFirstName')
    print(orderName)

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()
            if request.method == 'POST':
                      order_id = request.session.get('order_id')
                      first_name = request.session.get('orderFirstName')
                      last_name = request.session.get('orderLastName')
                      email = request.session.get('orderEmail')
                      address = request.session.get('orderAddress')
                      postal_code = request.session.get('orderPostalCode')
                      city = request.session.get('orderCity')
                      items = request.session.get('itemCount')
                      price = request.session.get('itemPrice')
                      products = request.session.get('productList')
                      ctx = {
                          'order_id': order_id,
                          'first_name': first_name,
                          'last_name': last_name,
                          'email': email,
                          'address': address,
                          'postal_code': postal_code,
                          'city': city,
                          'items': items,
                          'price': price,
                          'products': products,
                       }
            # create invoice e-mail
                      subject = 'Indian Express: online Pickup order confirmation - Order Number {}'.format(order.id)
                        #message = 'Thank you for shopping at Indianexpress.' \
                                  #'Your payment has been processed successfully. ' \
                                  #'Invoice no. {}'.format(order.id)
                      text = render_to_string('indianexpress/orderconfrim.txt',ctx)
                      print(text)
                      email = EmailMultiAlternatives(subject,text,
                                             'indian.xpress7@gmail.com',
                                             [order.email])

        #  # send e-mail

                      email.send()
            return redirect('payment:done')

        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = braintree.ClientToken.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
