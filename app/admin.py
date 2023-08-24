from flask import Blueprint, render_template, flash, session, redirect, \
    url_for, request
from db.models import Admins, Products, Orders, Shop, Details
from db import db
from app.utils import exportOrders, exportProducts

admin = Blueprint("admin", __name__, static_folder="static",
                  template_folder="templates")


@admin.route("/forward/<export>", methods=['POST'])
def forward(export):
    if export == 'orders':
        exportOrders()
    else:
        exportProducts()
    flash("Excel звіт створено.")
    return redirect(url_for("admin.view"))


@admin.route("/view")
@admin.route("/")
def view():
    if "id" in session:
        return render_template("view.html",
                               values=Admins.query.all(),
                               orders=Orders.query.all(),
                               shops=Shop.query.all(),
                               details=Details.query.all(),
                               product=Products.query.all(),
                               session=session
                               )
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("auth.login"))


@admin.route("/products", methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        # database
        query_params = request.args
        act = query_params.get('act')
        id_product = query_params.get('id')
        if act:
            if act == 'edit':
                product = Products.query.\
                    filter_by(id_product=id_product).first()
                product.title = request.form["title"]
                product.amount = request.form["amount"]
                flash("Продукт відредаговано!")
            elif act == 'add':
                title = request.form["title"]
                amount = request.form["amount"]
                pr = Products(title, amount)
                db.session.add(pr)
                flash("Продукт додано!")

            db.session.commit()
        return redirect(url_for("admin.products"))
    else:
        query_params = request.args
        act = query_params.get('act')
        id_product = query_params.get('id')
        if act:
            if act == 'edit':
                product = Products.query.\
                    filter_by(id_product=id_product).first()
                return render_template("products.html",
                                       values=Products.query.all(), edit=True,
                                       product=product)
            elif act == 'add':
                return render_template("products.html",
                                       values=Products.query.all(), add=True)
            elif act == 'delete':
                found_product = Products.query.filter_by(id_product=id_product)
                if found_product.delete():
                    db.session.commit()
                    flash("This product was deleted!", "info")
                else:
                    flash("This product isn't in db!", "info")
                return redirect(url_for("admin.products"))

        elif "id" in session:
            return render_template("products.html",
                                   products=Products.query.all())
        else:
            flash("You're not logged in", "info")
            return redirect(url_for("auth.login"))
