from flask import render_template, request, redirect

from flask_app import app
# import the class from dojo.py
from flask_app.models.dojo import Dojo


@app.route("/")
@app.route('/dojos')
def dojos():
    return render_template("new_dojo.html", dojos=Dojo.get_all())

# SEE ninjas.py
# @app.route('/ninja/new')
# def new():
#     return render_template("new_ninja.html")



# @app.route('/user/create', methods=['POST'])
# def create():
#     print(request.form)
#     User.save(request.form)
#     return redirect('/users')
#     #Note, remember, never 'render' on a POST

# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data = {
#         "id" : id
#     }
#     return render_template("edit_user.html", user=User.get_one(data))

@app.route('/ninjas/<int:id>')
def show(id):
    data = {
        "id" : id
    }
    return render_template("show_ninjas.html",dojo=Dojo.get_one(data))

# @app.route('/user/update', methods=['POST'])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/user/destroy/<int:id>')
# def destroy(id):
#     data = {
#         'id' : id
#     }
#     User.destroy(data)
#     return redirect('/users')