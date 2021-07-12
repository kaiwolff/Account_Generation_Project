from flask import Flask, request, abort, redirect, url_for, render_template
import jwt
app = Flask(__name__)

from user_account_details import UserAccountDetails

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

    new_user = UserAccountDetails()
    message = new_user.create_new_user(user_name, first_name, last_name, birth_year, password)

    return render_template("register_result.html",message=message)


@app.route('/login', methods = ['POST', 'GET'])
def login():

    if request.method == 'GET':
        return render_template("login.html")

    user_name = request.form.get('username')
    password = request.form.get('pwd')

    if user_login(user_name,password) == True:
        message = "Login successful"

        if check_admin(user_name, password)== True:
            return render_template("management_options.html")

    else:
        abort(403)
    return render_template("login_attempt.html",message = message )

@app.route('/manage/option', methods = ['POST'])
def select_management_option():

    #need to check for valid token

    #read in the format
    operation = request.form.get('operation')

    if operation == "delete":
        #render for to take in delete
        return render_template("delete_user.html")
    elif operation == "change_to_user":
        #render template for changing to user
        return render_template('change_to_user.html')
    elif operation == "change_to_manager":
        #render template for elevating to manager
        return render_template('change_to_manager.html')
    elif operation == "change_username":
        #render template for changing username
        return render_template("change_username.html")


@app.route('manage/option/change_to_manager', methods = ['POST', 'GET']) #/change/
def user_to_manager():
    if request.method == 'GET':
        return render_template('change_to_manager.html')

    user_name = request.form.get('username')
    manager_name = request.form.get('manger_name')
    manager_password = request.form.get('manager_password')

    user_details = UserAccountDetails()
    message = new_user.change_to_manager(user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)


@app.route('manage/option/change_to_user', methods = ['POST', 'GET']) #/change/
def manager_to_user():
    if request.method == 'GET':
        return render_template('change_to_user.html')

    user_name = request.form.get('username')
    manager_name = request.form.get('manager_name')
    manager_password = request.form.get('manager_password')

    user_details = UserAccountDetails()
    message = new_user.change_to_user(user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)


@app.route('manage/option/delete_user', methods = ['POST', 'GET']) #/change/
def user_delete():
    if request.method == 'GET':
        return render_template('delete_user.html')

    user_name = request.form.get('username')
    manager_name = request.form.get('manger_name')
    manager_password = request.form.get('manager_password')

    user_details = UserAccountDetails()
    message = new_user.delete_user(user_name, manager_name, manager_password)
    return render_template("management_result.html", message=message)


@app.route('manage/option/change_username', methods = ['POST', 'GET']) #/change/
def username_change():
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
    app.run(debug= True, host = '0.0.0.0', ssl_context = 'certs/pub_certs.pem', 'certs/priv_key.pem')
    NowTime = datetime.now() + timedelta(minutes = 72)
    NowTime = NowTime.isformat()
    Token = jwt.encode({
    'Username': username,
    'Expiry': NowTime,
    })  # needs secret key
