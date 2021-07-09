from flask import Flask, request, abort, redirect, url_for, render_template
app = Flask(__name__)

from user_account_details import UserAccountDetails

@app.route('/',methods = ['POST', 'GET'])
def welcome():
    return render_template("index.html")

    # choice = request.form.get('choice')
    # if choice == "Log in":
    #     return render_template("login.html")
    #
    # elif choice == "Register":
    #     return render_template("register.html")

@app.route('/register/success')
def register_success():
   return render_template("result_register_success.html")

@app.route('/register/fail')
def register_fail():
   return render_template("result_register_fail.html")

@app.route('/login/success')
def login_success():
    return 'Login successful.'

@app.route('/login/fail')
def login_fail():
    return render_template("result_login_fail.html")

@app.route('/change_to_manager/success')
def change_to_manager_success():
   return render_template("result_change_to_manager_success.html")

@app.route('/register',methods = ['POST', 'GET'])
def register():
    return render_template("register.html")
    # choice = request.form.get('choice', type=str)

    new_user = UserAccountDetails()
    message = new_user.create_new_user(user_name, first_name, last_name, birth_year, password)

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    birth_year = request.form.get('year')
    user_name = request.form.get('username')
    password = request.form.get('pwd')

    # here: try to register the user with the given details
    # Call create_new_user from the backend


    if message == "You have been successfully added to the database system.":
        return render_template("result_register_success.html")
        # take them to the success perform_change_name
    # elif message == "Your password is weak.":
    #     # take user to page with generated password
    #     return render_template("register.html")
    else:
        #take them to a failure page
        return render_template("result_register_fail.html")

    # take them to success or failure screen depending on message





@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")
    user_name = request.form.get('username')
    password = request.form.get('pwd')



@app.route('/change_to_manager') #/change/
def user_to_manager():
    return render_template('change_to_manager.html')

    user_details = UserAccountDetails()
    message = new_user.change_to_manager(user_name, manager_name, manager_password)

    user_name = request.form.get('username')
    manager_name = request.form.get('manger_name')
    manager_password = request.form.get('manager_password')

    if message == "The account has been changed to admin status.":
        return render_template('result_change_to_manager_success.html')

    else:
        return render_template('result_change_to_manager_fail.html')


@app.route('/change_to_user') #/change/
def manager_to_user():
    return render_template('change_to_user.html')

    user_details = UserAccountDetails()
    message = new_user.change_to_user(user_name, manager_name, manager_password)

    user_name = request.form.get('username')
    manager_name = request.form.get('manger_name')
    manager_password = request.form.get('manager_password')

    if message == "The account has been changed to user status.":
        return render_template('result_change_to_user_success.html')

    else:
        return render_template('result_change_to_user_fail.html')

# @app.route('/delete_user') #/change/
# def user_delete():
#     return render_template('delete_user.html')
#
#     user_details = UserAccountDetails()
#     message = new_user.delete_user(user_name, manager_name, manager_password)
#
#     user_name = request.form.get('username')
#     manager_name = request.form.get('manger_name')
#     manager_password = request.form.get('manager_password')
#
#     if message == "The account {} has been deleted from the database".format(user_name)
#         return render_template('delete_user_success.html')
#
#     else:
#         return render_template('result_change_to_user_fail.html')

# @app.route(/login/manager/<name>)
# def success(name):
#    return 'welcome %s' % name
#s
# @app.route(/login/user/<name>)
#
# @app.route(/action/<action>)
# def action(action)
#
#     if
#         return()
#
#     if action == ""
#
# _name_nameirth_erass







          # return a confimation success page
    # else:
    #     first = request.args.get('fname')
    #     return redirect(url_for('success',name = first))

    # new_user = UserAccountDetails()
    # return (new_user.create_new_user(user_name, first_name, last_name, birth_year))

# @app.route('/change_to_user/<str:user_name>/') #/change/
# def perform_change_to_user(target_user_name, manager_name, manager_password):
#     user_details = UserAccountDetails()
#     return (user_details.change_to_user(user_name),)


#
# @app.route('change_name/<str:old_user_name>/<str:new_user_name>')
# def perform_change_name(old_user_name, new_user_name):
#     user_details = UserAccountDetails()
#     return (user_details.perform_change_username(old_user_name, new_user_name))
#
# @app.route('/create/<str:username>/<str:fname>/<str:lname>/int<dobyear>')
# def perform_create_user(user_name, first_name, last_name, birth_year):
#     new_user = UserAccountDetails()
#     return (new_user.create_new_user(user_name, first_name, last_name, birth_year))

# @app.route('/delete/<str:username>')
# def perform_delete_user(user_name):
#     del_user = UserAccountDetails()
#     return (del_user.delete_new_user(user_name))


if __name__ == "__main__":
    app.run(debug= True, host = '0.0.0.0')

#LIST OF FUNCTIONS
# UserAccountDetails()
    # check_admin(self, user_name) # no need to use flask on this - called by other functions to confirm permission
    # change_access(self, user_name) - NEEDS FLASKING - split into change_to_user and change_to_manager
    # change_username(self, old_user_name, new_user_name) - NEEDS FLASKING
    # table_update(self, user_name) # changed to delete_new_user - NO NEED TO FLASK - OBSOLETE
    # delete_new_user(self, user_name) - NEEDS FLASKING
    # check_existence(self, user_name) - NO NEED TO FLASK
    # create_new_user(self,user_name,first_name,last_name,birth_year) - NEEDS FLASKING


# ## Completed from previous
# password_strength_prompt() # the same as check_policy - DEPENDENCY - NO NEED TO FLASK?

# UserPasswordDetails()
    # read_password_policy()
    # check_policy()
    # check_list()
    # check_user_details()
    # THE ABOVE FOUR DON'T NEED FLASKING
#63.35.225.165
