import email

import braintree

from django.shortcuts import render, redirect, get_object_or_404

from orders.forms import OrderCreateForm
from orders.models import Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
# import weasyprint
from io import BytesIO


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

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
            # create invoice e-mail
            subject = 'IndianExpress - Invoice no. {}'.format(order.id)
            message = 'Thank you for shopping at Indianexpress.' \
                      'Your payment has been processed successfully. ' \
                      'Invoice no. {}'.format(order.id)
            email = EmailMessage(subject,
                                 message,
                                 'indian.xpress7@gmail.com',
                                 [order.email])

            # if request.method == 'Get':
            #     form = OrderCreateForm(request.GET)
            #     if form.is_valid():
            #         first_name = form.cleaned_data.get('first_name')
            #         last_name = form.cleaned_data.get('last_name')
            #         email = form.cleaned_data.get('email')
            #         address = form.cleaned_data.get('address')
            #         postal_code = form.cleaned_data.get('postal_code')
            #         city = form.cleaned_data.get('city')
            #         ctx = {
            #             'first_name': first_name,
            #             'last_name': last_name,
            #             'email': email,
            #             'address': address,
            #             'postal_code': postal_code,
            #             'city': city,
            #         }
            #
            # message = render_to_string('indianexpress/orderconfrim.txt', ctx)
            # send_mail('Your Order with IndianXpress',
            #             message,
            #             'indxpr@gmail.com',
            #             [email],)
            # return render(request, 'payment/done.html', ctx)
            #




        #
        #
        #  # create invoice e-mail
        #  subject = 'Indianexpress - Invoice no. {}'.format(order.id)
        #
        #  message = 'Thank you for shopping at Indianexpress.' \
        #            ' Your payment has been processed successfully. ' \
        #            'Invoice no. {}'.format(order.id)
        #
        #  email = EmailMessage(subject,
        #                       message,
        #                       'indian.xpress7@gmail.com',
        #                       [order.email])
        #  # generate PDF
        #  # html = render_to_string('orders/order/pdf.html', {'order': order})
        #  # out = BytesIO()
        #  # stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
        #  # weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
        #
        #  # attach PDF file
        # # email.attach('order_{}.pdf'.format(order.id),
        # #              out.getvalue(),
        # #              'application/pdf')
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
