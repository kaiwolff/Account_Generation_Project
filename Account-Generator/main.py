from flask import Flask, request, abort, redirect, url_for, render_template, jsonify, make_response

# Token imports
import jwt

# System imports
from datetime import datetime, timedelta

from user_account_details import UserAccountDetails
import decorators

app = Flask(__name__)

def manager_token(token):
    #decode token, read manager field, return True or False depending on outcome.
    decoded_token = jwt.decode(token, 'SECRET_KEY_123456798', 'HS256')
    if decoded_token['Manager'] == 'yes':
        print("you are a manager")
        return True
    else:
        print("you are not a manager")
        return False

@app.route('/',methods = ['POST', 'GET'])
def welcome():
    return render_template("index.html")


@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    birth_year = request.form.get('year')
    user_name = request.form.get('username')
    password = request.form.get('pwd')

    print(user_name, first_name, last_name, birth_year, password)

    new_user = UserAccountDetails()
    message = new_user.create_new_user(user_name, first_name, last_name, birth_year, password)

    return render_template("register_result.html",message=message)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    user= UserAccountDetails()
    if request.method == 'GET':
        #check token
        return render_template("login.html")

    user_name = request.form.get('username')
    password = request.form.get('pwd')

    if user.user_login(user_name,password) == True:

        message = "Login successful"

        if user.check_admin(user_name, password)== True:
            print("survived admin check")
            NowTime = str(datetime.now() + timedelta(minutes = 72))
            print(NowTime)
            token = jwt.encode({
                'Username': user_name,
                'Expiry': NowTime,
                'Manager': 'yes',
            },'SECRET_KEY_123456798', algorithm= 'HS256')
            print(token)
            return render_template("login.html",myToken=token)

        else:
            NowTime = str(datetime.now() + timedelta(minutes = 72))
            token = jwt.encode({
                'Username': user_name,
                'Expiry': NowTime,
                'Manager': 'no',
            },'SECRET_KEY_123456798', algorithm= 'HS256')
            print(token) # needs secret key
            return render_template("login.html",myToken = token)

    else:
        abort(403)

# remember to add log out button that deletes token
@app.route('/dashboard', methods=['GET','POST'])
@decorators.token_required

def dashboard(username):
    headers = {'Content-Type': 'text/html'}
    token=request.args.get('myToken')

    if manager_token(token):
        return render_template('management_options.html', myToken=token)

    else:
        return make_response(render_template('user_dashboard.html'), 200, headers)


@app.route('/manage/option', methods = ['GET','POST'])
@decorators.token_required
def select_management_option(*args):

    if request.method == "GET":
        token = request.args.get('myToken',type=str)
        print("The token in GET form is {}".format(token))
        return render_template("management_options.html", myToken = token)

    if not manager_token(token):
        abort(403)

    #need to check for valid token

    #read in the format
    operation = request.form.get('operation')
    token = request.args.get('myToken',type=str)
    print("passing option to form. Token is {}".format(token))

    if operation == "delete":
        #render for to take in delete
        return render_template("delete_user.html", myToken=token)
    elif operation == "change_to_user":
        #render template for changing to user
        return render_template('change_to_user.html', myToken=token)
    elif operation == "change_to_manager":
        #render template for elevating to manager
        return render_template('change_to_manager.html', myToken=token)
    elif operation == "change_username":
        #render template for changing username
        return render_template("change_username.html", myToken=token)


@app.route('/manage/option/change_to_manager', methods = ['POST', 'GET']) #/change/
@decorators.token_required
def user_to_manager():


    if not manager_token(token):
        abort(403)
    if request.method == 'GET':
        return render_template('change_to_manager.html', myToken = token)

    user_name = request.form.get('username')
    manager_name = request.form.get('manager_name')
    manager_password = request.form.get('manager_password')


    user_details = UserAccountDetails()
    message = new_user.change_to_manager(user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)


@app.route('/manage/option/change_to_user', methods = ['POST', 'GET']) #/change/
@decorators.token_required
def manager_to_user():
    if not manager_token(token):
        abort(403)
    if request.method == 'GET':
        return render_template('change_to_user.html')

    user_name = request.form.get('username')
    manager_name = request.form.get('manager_name')
    manager_password = request.form.get('manager_password')

    user_details = UserAccountDetails()
    message = new_user.change_to_user(user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)


@app.route('/manage/option/delete_user', methods = ['POST', 'GET']) #/change/
@decorators.token_required
def user_delete(*args):
    if not manager_token(token):
        abort(403)
    if request.method == 'GET':
        return render_template('delete_user.html')

    user_name = request.form.get('username')
    manager_name = request.form.get('manager_name')
    manager_password = request.form.get('manager_password')

    user_details = UserAccountDetails()
    message = new_user.delete_user(user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)


@app.route('/manage/option/change_username', methods = ['POST', 'GET']) #/change/
@decorators.token_required
def username_change():
    if not manager_token(token):
        abort(403)
    if request.method == 'GET':
        return render_template('change_username.html')

    old_user_name = request.form.get('username')
    new_user_name = request.form.get('new_username')
    manager_name = request.form.get('manager_name')
    manager_password = request.form.get('manager_password')

    user_details = UserAccountDetails()
    message = new_user.change_username(old_user_name, new_user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)



if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0', ssl_context = ('certs/pub_cert.pem', 'certs/priv_key.pem'))
