from apiapplication import app
from projectfiles.apiapplication.models import Cart


def response_serializer(value):
    output = []
    for prod,cat,usr in value:
        output.append({
        'category':{
            'category_id':cat.category_id,
            'category_name':cat.category_name
        },
        'price':prod.price,
        'product_id':prod.product_id,
        'product_name':prod.product_name,
        'seller_id':usr.user_id
        

    })
    return output



def cartresponseserializer(value:Cart):

    for val in value:

