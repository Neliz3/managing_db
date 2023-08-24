from flask import Blueprint, render_template, request, redirect, \
    url_for, session, flash
from db import db
from db.models import Admins

auth = Blueprint("auth", __name__, static_folder="static",
                 template_folder="templates")


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # db
        email = request.form["email"]
        session.permanent = True
        session["email"] = email
        found_user = Admins.query.filter_by(email=email).first()
        if found_user:
            _password = request.form["pswd"]
            if _password == found_user.password:
                id_ = found_user.id_
                session["id"] = id_
                flash("Login successful", "info")

                return redirect(url_for("admin.view"))
            else:
                flash("You entered a wrong password. Try again, please.",
                      "info")
                return redirect(url_for("auth.login", alert='forgot_password'))
        else:
            flash("You are a new user. Welcome to registration page :)",
                  "info")
            return redirect(url_for("auth.registration"))
    else:
        email = None if 'email' not in session else session['email']
        if "id" in session:
            return redirect(url_for("admin.view"))
        elif request.args:
            return render_template("login.html", email=email,
                                   alert=request.args['alert'])
        else:
            return render_template("login.html", email=email)


@auth.route("/signup", methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        # Try/except unique of name/...
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["pswd"]

        usr = Admins(first_name, last_name, email, password)
        db.session.add(usr)
        db.session.commit()

        session.permanent = True
        session["id"] = usr.id_

        flash("Thanks for the registration!")
        return redirect(url_for("admin.view"))
    else:
        email = None if 'email' not in session else session['email']
        return render_template("signup.html", email=email)


@auth.route("/logout")
def logout():
    flash("You have been log out!", "info")
    session.pop("id", None)
    session.pop("email", None)
    return redirect(url_for("auth.login"))


@auth.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    email = None if 'email' not in session else session['email']
    if request.method == "POST":
        password = request.form["pswd"]
        try:
            usr = Admins.query.filter_by(email=email).first()
            usr.password = password
            db.session.commit()
            flash("Password was updated!")
        except Exception as ex:
            return f"{ex}"
        return redirect(url_for("auth.login"))
    else:
        return render_template("forgot_password.html", email=email)
