import re
from urllib import request
from . import api,db
from flask_restful import Resource
from flask import jsonify, request
from .serializer import response_serializer, cart_serializer
from .models import Product, Cart,CartProduct, Category,User,Role


class PublicSearchItem(Resource):
    def get(self,keyword):
        query = db.session.query(Product,Category,User).\
        select_from(Product).join(Category).join(User).filter(Product.product_name==keyword).all()
        print(query) 
        result_set = response_serializer(query)
        return jsonify(result_set)

api.add_resource(PublicSearchItem, '/api/public/product/search/<string:keyword>')



class CartItem(Resource):
    def get(self):
        query = db.session.query(Cart).all()
        print(query)
        resultset = cart_serializer(query)
        return jsonify(resultset)

api.add_resource(CartItem, '/api/public/cart')        


class PublicLogin(Resource):
    def post(self,username,password):
        username = request.json.get("username")
        password = request.json.get("password")

api.add_resource(PublicLogin,'/api/public/login')
# class PublicLogin(Resource):
#     def post(self, )