from flask import render_template, request, session, flash
from app import app
from db import db
from db.models import Shop, Orders, Details, Products
import datetime


@app.route("/shop", methods=['GET', 'POST'])
def shop():
    if request.method == "POST":
        shops = request.form["shop"]
        product_id = request.form.get('product')
        amount = request.form["amount"]

        found_shop = Shop.query.filter_by(name=shops).first()
        today = datetime.date.today()
        year = today.year

        id_shop = None
        if not found_shop:
            shp = Shop(shops)
            db.session.add(shp)
            db.session.flush()
            db.session.commit()
            id_shop = shp.id_shop
        else:
            id_shop = found_shop.id_shop

        order = Orders(id_shop, year)
        db.session.add(order)
        db.session.flush()
        db.session.commit()

        details = Details(order.id_order, product_id, amount)
        db.session.add(details)
        db.session.commit()

        session.permanent = True
        session["shop"] = shops

        if "new_product" in request.form:
            prod = request.form["new_product"]
            num = request.form["new_amount"]
            session["new_product"] = {prod: num}

        flash("Заявка подана!")
        return render_template("shop_orders.html", list=Products.query.all())
    else:
        return render_template("shop_orders.html", list=Products.query.all())
