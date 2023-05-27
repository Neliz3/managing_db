from flask import Blueprint, render_template, flash, session, redirect, url_for
from db.models import Users
from db import db

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")


@admin.route("/view")
@admin.route("/")
def view():
    if "email" in session:
        # email = session["email"]
        # if email == admin:
            # return redirect(url_for("admin.view"))
        return render_template("view.html", values=Users.query.all())
        # else:
        #     flash("You're not an admin", "info")
        #     return redirect(url_for("auth.login"))
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("auth.login"))


@admin.route("/delete/<name>")
def delete(name):
    if "email" in session:
        email = session["email"]
        if email == admin:
            # db
            found_user = Users.query.filter_by(name=name)
            if found_user.delete():
                db.session.commit()
                flash("This user was deleted!", "info")
            else:
                flash("This name isn't in db!", "info")

            return render_template("view.html", values=Users.query.all())
        else:
            flash("You're not an admin", "info")
            return redirect(url_for("auth.login"))
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("auth.login"))
