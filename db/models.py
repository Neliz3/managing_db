from db import db


class Admins(db.Model):
    __tablename__ = "admins"

    id_ = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Shop(db.Model):
    __tablename__ = "shop"

    id_shop = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    orders = db.relationship("Orders", back_populates="shop")

    def __init__(self, name):
        self.name = name


class Products(db.Model):
    __tablename__ = "products"

    id_product = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    amount = db.Column(db.Integer)
    details = db.relationship("Details", back_populates="product")

    def __init__(self, title, amount):
        self.title = title
        self.amount = amount


class Orders(db.Model):
    __tablename__ = "orders"

    id_order = db.Column(db.Integer, primary_key=True)
    id_shop = db.Column(db.Integer, db.ForeignKey('shop.id_shop'), nullable=False)
    year_order = db.Column(db.Integer)
    details = db.relationship('Details', back_populates='orders')
    shop = db.relationship("Shop", back_populates="orders")

    def __init__(self, id_shop, year_order):
        self.id_shop = id_shop
        self.year_order = year_order


class Details(db.Model):
    __tablename__ = "details"

    id = db.Column(db.Integer, primary_key=True)
    id_order = db.Column(db.Integer, db.ForeignKey('orders.id_order'), nullable=False)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id_product'), nullable=False)
    quantity = db.Column(db.Integer)
    orders = db.relationship("Orders", back_populates="details")
    product = db.relationship("Products", back_populates="details")

    def __init__(self, id_order, id_product, quantity):
        self.id_order = id_order
        self.id_product = id_product
        self.quantity = quantity
