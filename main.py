from flask import Flask, session, url_for, render_template, redirect, request

from genre_dictionary import genre_dict
import os


my_secret = os.environ['SECRET_KEY']


app = Flask(__name__)
app.secret_key = my_secret





@app.route("/")
def hello_world():

    


    return render_template("index.html", genre_dict=genre_dict)



@app.route("/myatlas/<username>", methods=["POST", "GET"])
def myatlas(username):
    
    
    
    return render_template("myatlas.html", username=username)


@app.route("/login", methods=["POST", "GET"])
def login():

    login_form = LoginForm()    

    if login_form.validate_on_submit():

        if request.method == "POST":
            
            entered_username = login_form.username.data
            entered_password = login_form.password.data

            print(entered_username, entered_password)
    
            if entered_username in list(db.keys()):
            
                session["username"] = login_form.username.data
                session["password"] = login_form.password.data
                session.modified = True
                return redirect(url_for("myatlas", username=username))
            else:
                return redirect(url_for("signup"))
    
    
    return render_template("login.html", login_form=login_form)

@app.route("/signup", methods=["POST", "GET"])
def signup():

    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        entered_username = signup_form.username.data
        entered_password = signup_form.password.data

        session["username"] = entered_username
        session["password"] = entered_password

        if entered_username in db.keys():
            return "Username already exists"
        else:
            db[entered_username] = entered_password


        return redirect(url_for("myatlas"))
    
    return render_template("signup.html", signup_form=signup_form)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

