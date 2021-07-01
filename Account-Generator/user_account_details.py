class UserAccountDetails():

    def check_admin(self, user_name):# check if the admin value is true
        pass

    def change_access(self, user_name): # changes the value of admin role column
        pass

    def change_username(self, old_user_name, new_user_name): # only if the user is an admin, allows to change the user name

        pass

    def delete_new_user(self, user_name): # deletes user details

        #with connect(host="localhost", user="root", password=sql_password, database="User_database.db") as connection:

              with connection.cursor()as cursor:
                  command = f"DELETE FROM User_database WHERE UserName= '{user_name}';"
                  cursor.execute(command)
                  cursor.close()
                  pass

    def check_existence(self, user_name): # checks if a user exists in a database

        with connect(host="localhost", user="root", password=sql_password, database="User_database.db") as connection:

              with connection.cursor()as cursor:
                  command = f"SELECT * FROM `User_database` WHERE UserName= '{user_name}';"
                  cursor.execute(command)
                  cursor.fetchall()
                  num_occurences = cursor.rowcount
                  # print("num_occurences assigned")
                  cursor.close()

              if num_occurences > 0:
                  return True
              elif num_occurences == 0:
                  return False

    def create_new_user(self,user_name,first_name,last_name,birth_year): # creates user details

        with connect(host="localhost", user="root", password=sql_password, database="User_database.db") as connection:

              with connection.cursor()as cursor:
                  command = f"INSERT INTO User_database (UserName, FirstName, LastName, BirthYear) VALUES ('{user_name}, '{first_name}', '{last_name}', '{birth_year}');"
                  cursor.execute(command)
                  cursor.close()
                  pass
