# specify amount selected from mysql table
# SELECT * FROM `users` LIMIT 30;
# order by the student's name alphabetical asc
# SELECT * FROM students ORDER BY name ASC LIMIT 0, 20;

# https://www.plus2net.com/python/tkinter-mysql-paging.php
# from sqlalchemy import create_engine
# my_conn = create_engine("mysql+mysqldb://userid:password@localhost/db_name")
# ###### end of connection ####
# r_set=my_conn.execute("SELECT count(*) as no from STUDENT")
# data_row=r_set.fetchone()
# no_rec=data_row[0] # Total number of rows in table
# limit = 8; # No of records to be shown per page.
# ##### tkinter window ######
# import tkinter  as tk
# from tkinter import *
# my_w = tk.Tk()
# my_w.geometry("350x200")
# def my_display(offset):
#
#     q="SELECT * from student LIMIT "+ str(offset) +","+str(limit)
#     r_set=my_conn.execute(q);
#     i=0 # row value inside the loop
#     for student in r_set:
#         for j in range(len(student)):
#             e = Entry(my_w, width=10, fg='blue')
#             e.grid(row=i, column=j)
#             e.insert(END, student[j])
#         i=i+1
#     while (i= 0):
#         b2["state"]="active"  # enable Prev button
#     else:
#         b2["state"]="disabled"# disable Prev button
# my_display(0)
# my_w.mainloop()

# @app.route('/images', defaults={'page':1})
# @app.route('/images/page/<int:page>')
# def abc(page):
#     perpage=20
#     startat=page*perpage
#     db = mysql.connect('localhost', 'root', 'password', 'img')
#     cursor = db.cursor()
#     cursor.execute('SELECT Id,Title,Img FROM image limit %s, %s;', (startat,perpage))
#     data = list(cursor.fetchall())



from flask import Flask, request, abort, redirect, url_for, render_template, jsonify, make_response

from mysql.connector import connect, Error
from pprint import pprint
from sql_init import sql_DB
import jwt

# System imports
from datetime import datetime, timedelta

from user_account_details import UserAccountDetails
import decorators

app = Flask(__name__)

@app.route('/manage/option', methods = ['GET','POST'], defaults={'page':1})
@app.route('/manage/option/page<int:page>')
@decorators.manager_token_required
def select_users(token, username, page):
    if request.method == "GET":
        print("The token in GET form is {}".format(token))
        message = "Welcome to Management options"
        return render_template("management_options.html", myToken = token,message = message)

    #user_name = request.form.get('username')
    perpage = 20
    startat = page*perpage
    db = sql_DB()
    cursor = db.cursor
    command = "SELECT `username`, `Manager` FROM `user_info` ORDER BY `username` ASC LIMIT '{}', '{}';".format(startat, perpage)
    cursor.execute(command)
    db.connection.commit()
    data = list(cursor.fetchall())
    db.close_down()
    pprint(data)

    # if operation == "delete":
    #     user = UserAccountDetails()
    #     #render for to take in delete
    #     message = user.delete_user(user_name)
    #     print(message)
    #     return make_response(jsonify(message),200)
    # elif operation == "change_to_user":
    #     user = UserAccountDetails()
    #     message = user.change_to_user(user_name)
    #     print(message)
    #     return make_response(jsonify(message),200)
    # elif operation == "change_to_manager":
    #     user = UserAccountDetails()
    #     message = user.change_to_manager(user_name)
    #     print(message)
    #     return make_response(jsonify(message),200)
