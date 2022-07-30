# imports

from flask import Blueprint, redirect, render_template, request, url_for, jsonify,session
import ass4_db
# blue print
assignment4 = Blueprint(
    "assignment4",
    __name__,
    static_folder="static",
    static_url_path="/assignment4",
    template_folder="templates",
)


# routes
@assignment4.route('/')
@assignment4.route("/home",  methods=['GET'])
def home():
    return render_template('Home_Page.html', username=session.get('username'))



@assignment4.route("/Assignment4",  methods=['GET'])
def Assignment4():
    return render_template('assignment4.html')

@assignment4.route("/insert_user",  methods=['POST'])
def insert_user():
    # insert user
    if request.method == "POST":
        _id = int(request.form["id"])
        passwd = request.form["passwd"]
        name = request.form["name"]
        email = request.form["email"]

        try:
            res = ass4_db.insert_user(_id, name, email, passwd)
        except:
            res = False
        if res:
            return render_template('assignment4.html',
                                   users=[request.form],
                                   alert='warning')
        else:
            return render_template('assignment4.html',
                                   message='insert not done')


@assignment4.route("/delete_user",  methods=['POST'])
def delete_user():
    _id = int(request.form["id"])
    res = ass4_db.get_user_by_id(str(_id))
    if res:
        ass4_db.delete_user(_id)
        return render_template('assignment4.html', users=[request.form],  alert='warning')
    else:
        return render_template('assignment4.html', message='NO ITEM FOUND TO DELETE')



@assignment4.route("/update_user",  methods=['GET','POST','PUT'])
def update_user():
    print(request.form)
    _id = int(request.form["id"])
    passwd = request.form["passwd"]
    name = request.form["name"]
    email = request.form["email"]

    res = ass4_db.get_user_by_id(str(_id))
    if res:
        ass4_db.update_user(_id, name, email, passwd)
        return render_template('assignment4.html',users=[request.form],  alert='warning')
    else:
        return render_template('assignment4.html', message='NO UPDATE')


users_dict = {}
@assignment4.route("/list_users",  methods=['GET'])
def list_user():
    res=ass4_db.get_users()
    return render_template('assignment4.html',
                           users=res)