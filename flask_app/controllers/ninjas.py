from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninja/new')
def new_ninja_page():
    return render_template("new_ninja.html", all_dojos = Dojo.get_all())


@app.route('/ninjas/new', methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)

    return redirect("/")
