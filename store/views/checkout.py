from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.core.mail import  EmailMessage
from django.core.mail import send_mail, BadHeaderError
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        customer = request.session.get('customer')
        if customer:
                name = request.POST.get('name')
                email = request.POST.get('email')
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                customer = request.session.get('customer')
                cart = request.session.get('cart')
                products = Product.get_products_by_id(list(cart.keys()))
                prod = 0
                for product in products:
                    product
                    prod += product.price * cart.get(str(product.id))
                order = Order.objects.create(
                    name=name,
                    email=email,
                    address=address,
                    phone=phone,
                    price=prod,
                    customer=Customer(id=customer)
                )
                for product in products:
                  sub = Product.objects.get(name=product)
                  order.product.add(sub)
                order.save()
                all_products = []
                for product in products:
                    all_products.append(product)
                emails = EmailMessage(f'Hi Mr.Talha',f'Customer have checkout successfully:\n His Address {address}\nHis phone {phone}\n'
                                      f'His Cart ID {cart}\nHis AllProducts {all_products}',
                                      'noreply@semycolon.com', ['talhasarwar289@gmail.com'], )
                emails.send()
                request.session['cart'] = {}
                return redirect('cart')
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))
            prod = 0
            for product in products:
                product
                prod += product.price * cart.get(str(product.id))
            order = Order.objects.create(
                name=name,
                email=email,
                address=address,
                phone=phone,
                price=prod,
            )
            for product in products:
                sub = Product.objects.get(name=product)
                order.product.add(sub)
            order.save()
        all_products = []
        for product in products:
            all_products.append(product)
        emails = EmailMessage(f'Hi Mr.Talha',
                              f'{name} ,Customer, have checkout successfully:\n His Address {address}\nHis phone {phone}\n'
                              f'His Cart ID {cart}\nHis All Products {all_products}',
                              'noreply@semycolon.com', ['talhasarwar289@gmail.com'], )
        emails.send()
        request.session['cart'] = {}
        return redirect('cart')
