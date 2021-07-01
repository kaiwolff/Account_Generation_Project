class UserAccountDetails():

    def check_admin():# check if the admin value is true
        pass

    def change_access(): # changes the value of admin role column
        pass

    def change_username(): # only if the user is an admin, allows to change the user name

        pass

    def delete_new_user(): # deletes user details
        pass

    def check_existence(self, user_name): # checks if a user exists in a database

        with connect(host="localhost", user="root", password=sql_password, database="common_password_db") as connection:

              with connection.cursor()as cursor:
                  command = f"SELECT * FROM `common_passwords` WHERE password = '{password}';"
                  cursor.execute(command)
                  cursor.fetchall()
                  print(cursor.rowcount)
                  print(password)
                  num_occurences = cursor.rowcount
                  # print("num_occurences assigned")
                  cursor.close()

              if num_occurences > 0:
                  return False
              elif num_occurences == 0:
                  return True

    def create_new_user(): # creates user details
        pass
