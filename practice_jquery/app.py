from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL #pip install flask-mysql
import pymysql

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'my_secret_password'
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def home():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from users order by id")
        userslist = cursor.fetchall()
        return render_template('index.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route("/update",methods=["POST","GET"])
def update():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            field = request.form['field']
            value = request.form['value']
            editid = request.form['id']

            if field == 'username':
               sql = "UPDATE users SET username=%s WHERE id=%s"
            if field == 'name':
                sql = "UPDATE users SET name=%s WHERE id=%s"

            data = (value, editid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run()
