from urllib import request
from . import api, db, jwt, app
from flask_restful import Resource
from flask import jsonify, request
from .serializer import response_serializer, cart_serializer
from .models import Product, Cart, CartProduct, Category, User, Role
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from .validators import validate_number

app.config["JWT_SECRET_KEY"] = "useridkey"
tokenAuth = {}


class PublicSearchItem(Resource):
    def get(self, keyword):
        query = db.session.query(Product, Category, User).\
            select_from(Product).join(Category).join(User).filter(
                Product.product_name == keyword).all()
        print(query)
        result_set = response_serializer(query)
        return jsonify(result_set)


api.add_resource(PublicSearchItem,
                 '/api/public/product/search/<string:keyword>')


class CartItem(Resource):
    def get(self):
        query = db.session.query(Cart).all()
        print(query)
        resultset = cart_serializer(query)
        return jsonify(resultset)


api.add_resource(CartItem, '/api/public/cart')


class PublicLogin(Resource):
    def post(self):

        username = request.headers["username"]
        print("username", username)
        password = request.headers["password"]
        print("password", password)

        user = db.session.query(User).filter(
            User.user_name == username, User.password == password).all()

        print("user", user)

        if not user:
            print('User not found')

        for usr in user:
            print("printing user data from db")
            dbuser = usr.user_name
            dbpassword = usr.password
            print(dbuser, "::", dbpassword)
            # id = dbuser+dbpassword
            access_token = create_access_token(identity=dbuser)
            tokenAuth.update({"Authorization": "Bearer "+access_token})

        return jsonify({"access_token": access_token})


api.add_resource(PublicLogin, '/api/public/login')


class CurrentUser(Resource):
    @jwt_required()
    # def get(self):
    #     headers = request.headers
    #     bearer = headers.get("Authorization")
    #     token = headers.split()[1]
    #     currentuser = get_jwt_identity()
    def get(self):
        # headers = request.headers
        # bearer = headers.get('Authorization')    # Bearer YourTokenHere
        # token = bearer.split()[1]
        currentuser = get_jwt_identity()

        print("currentuser", currentuser)
        # print("token : ", token)
        return jsonify({"currentuser": currentuser, "tokenAuth": tokenAuth})


api.add_resource(CurrentUser, '/api/currentuser')

# Seller end points


class SellerProduct(Resource):
    @jwt_required()
    def get(self):
        resultset = ''
        currentuser = get_jwt_identity()

        currentuserrole = db.session.query(
            User).select_from(User).filter(User.user_name == currentuser)
        print("currentuserrole", currentuserrole)
        if currentuserrole:
            for val in currentuserrole:
                print("val", val)
                role_id = val.user_role
                print("role_id", role_id)
                user_name = val.user_name
                print(user_name)
                if role_id == 2:
                    user_id = validate_number(val.user_id)

                    print("user_id", user_id)

                    queryresult = db.session.query(Product, Category, User).\
                        select_from(Product).join(Category).join(User).filter(
                        Product.seller_id == user_id).all()

                    print("queryresult", queryresult)

                    if queryresult:
                        resultset = response_serializer(queryresult)
                else:
                    return jsonify({"message": "Hello!!! "+user_name+" Only Sellers allowed , please login with seller id "})

            return jsonify(resultset)

    @jwt_required()
    def put(self):
        result_set = ''
        currentuser = get_jwt_identity()
        currentuserrole = db.session.query(User).select_from(User).filter(
            User.user_name == currentuser)
        print("currentuserrole", currentuserrole)


api.add_resource(SellerProduct, '/api/auth/seller/product')


# class SellerProductId(Resource):
#     @jwt_required
#     def get():
#         result_set = ''
#         current_user = get_jwt_identity()
#         currentuserrole = db.session.query(User).select_from(
#             User).filter(User.user_name == current_user)
#         print("currentuserrole", currentuserrole)

#         if currentuserrole:
