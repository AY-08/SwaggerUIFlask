import re
from apiapplication import api,db
from flask_restful import Resource
from flask import jsonify
from apiapplication.serializer import response_serializer
from apiapplication.models import Product, Cart,CartProduct, Category,User,Role


class PublicSearchItem(Resource):
    def get(self,keyword):
        query = db.session.query(Product,Category,User).\
        select_from(Product).join(Category).join(User).filter(Product.product_name==keyword).all()
        print(query) 
        result_set = response_serializer(query)
        return jsonify(result_set)

api.add_resource(PublicSearchItem, '/api/public/product/search/<string:keyword>')



class CartItem(Resource):
    def get():
        query = db.session.query(Cart).all()
        print(query)
        resultset = cartresponseserializer(query)
        return jsonify(resultset)
# class PublicLogin(Resource):
#     def post(self, )