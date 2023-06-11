from . import app
from .models import Cart, CartProduct


def response_serializer(value):
    output = list()
    for prod, cat, usr in value:
        output.append({
            'category': {
                'category_id': cat.category_id,
                'category_name': cat.category_name
            },
            'price': prod.price,
            'product_id': prod.product_id,
            'product_name': prod.product_name,
            'seller_id': usr.user_id


        })
    return output


def cart_serializer(value: Cart):
    output = list()

    for val in value:
        response_dict = {'cart_id': val.cart_id,
                         'totalamount': val.totalamount,
                         'user_id': val.user_id,
                         'cartproduct': cartproduct_serializer(val.cartproduct)
                         }

        output.append(response_dict)

    return output


def cartproduct_serializer(value: CartProduct):
    output = list()

    for val in value:
        response_dict = {'cp_id': val.cp_id,
                         'cart_id': val.cart_id,
                         'product_id': val.product_id,
                         'quantity': val.quantity
                         }

        output.append(response_dict)

    return output
