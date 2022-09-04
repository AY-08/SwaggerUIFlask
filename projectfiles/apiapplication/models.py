from apiapplication import db

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.String)
    user = db.relationship('User',backref = 'role',uselist = False)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)
    user_role= db.Column(db.Integer, db.ForeignKey('role.role_id'))
    product= db.relationship('Product',backref = 'user')
    cart= db.relationship('Cart',backref = 'user')

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
    product= db.relationship('Product',backref = 'category')


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    product_name = db.Column(db.String)
    category_id= db.Column(db.Integer, db.ForeignKey('category.category_id'))
    seller_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    cartproduct= db.relationship('CartProduct',backref = 'product')

class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    totalamount = db.Column(db.Numeric)
    user_id=db.Column(db.Integer,db.ForeignKey('user.user_id'))
    cartproduct = db.relationship('CartProduct',backref = 'cart')


class CartProduct(db.Model):
    cp_id = db.Column(db.Integer, primary_key=True)
    cart_id= db.Column(db.String, db.ForeignKey('cart.cart_id'))
    product_id = db.Column(db.Integer,db.ForeignKey('product.product_id'))
    quantity=db.Column(db.Integer)
