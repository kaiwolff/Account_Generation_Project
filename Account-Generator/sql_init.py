from mysql.connector import connect, Error
from hashfunctions import HashFunctions

class sql_DB:

    def __init__(self):
        with open("config_sql", "r") as file:
            configs = file.readlines()
            file.close()
        with open(".my_sql_password", "r") as file:
            sqlpassword = file.read()
            file.close()

        self.connection = connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db")
        self.cursor = self.connection.cursor()

# def check_admin(user_name, user_password):  # check if the admin value is true
#         # NEED TO RETRIEVE SALT, THEN HASH AND CHECK FOR CORRECT PASSWORDS
#
#         command = "SELECT * FROM `user_info` WHERE `username`= '{}' AND `password`='{}' AND `Manager` = 1;".format(
#             user_name,  HashFunctions().get_user_pass(user_name))
#         db = sql_DB()
#         db.cursor.execute(command)
#         #connection.commit()
#         db.cursor.fetchall()
#         num_occurences = db.cursor.rowcount
#         # print("num_occurences assigned")
#         db.cursor.close()
#         # print(HashFunctions().get_user_pass(user_name))
#         if num_occurences > 0:
#             return True
#         elif num_occurences == 0:
#             return False

print(check_admin("admin", "Lm(6QXlaYsk8"))#Works, returns True if admin details are correct
