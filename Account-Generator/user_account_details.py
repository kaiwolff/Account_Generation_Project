from mysql.connector import connect, Error


class UserAccountDetails():
    # pw_user_db, user_info, username, FirstName, LastName, BirthYear, password, Manager

    def check_admin(self, user_name, user_password):# check if the admin value is true

        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            with connection.cursor() as cursor:
                command = "Test"
                cursor.execute(command)
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()

                if num_occurences > 0:
                    return True
                elif num_occurences == 0:
                    return False


    def check_existence(self, user_name): # checks if a user exists in a database

        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            with connection.cursor()as cursor:
                command = f"SELECT * FROM `user_info` WHERE `username`= '{user_name}';"
                cursor.execute(command)
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()

                if num_occurences > 0:
                    return True
                elif num_occurences == 0:
                    return False

    def create_new_user(self, user_name, first_name, last_name, birth_year, password, manager_name, manager_password): # creates user details
        #check_admin()
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_existence(user_name):
                return f"{user_name} already exists."

            elif check_admin(manager_name, manager_password):

                with connection.cursor()as cursor:
                    command = f"INSERT INTO `user_info` (username, FirstName, LastName, password, BirthYear) VALUES ('{user_name}, '{first_name}', '{last_name}', '{password}', '{birth_year}');"
                    cursor.execute(command)
                    cursor.close()
                    return f"The user {user_name} has been added to the database."
            else:
                return f"You require an admin level account to create a new user."

    def change_to_manager(self, user_name, manager_name, manager_password): # changes the value of user role back to manager role
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_admin(manager_name, manager_password):
                with connection.cursor()as cursor:
                    command = f"UPDATE `user_info` SET `Manager`= 1 WHERE `username` = '{user_name}';"
                    cursor.execute(command)
                    cursor.close()
                    return f"{user_name} has been changed to admin status."

            else:
                return "You require an admin level account to change from user to admin status."

    def change_to_user(self, user_name, manager_name, manager_password): # changes the value of manager role back to user role
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_admin(manager_name, manager_password):
                with connection.cursor()as cursor:
                    command = f"UPDATE `user_info` SET `Manager` = 0 WHERE `username` = '{user_name}';"
                    cursor.execute(command)
                    cursor.close()
                    return f"{user_name} has been changed to user"

            else:
                return "You require an admin level account to update user status."


    def change_username(self, old_user_name, new_user_name, manager_name, manager_password): # only if the user is an admin, allows to change the user name
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:
            if check_admin(manager_name, manager_password):

                with connection.cursor()as cursor:
                    command = f"UPDATE `user_info` SET `username` = '{new_user_name}' WHERE `username` = '{old_user_name}';"
                    cursor.execute(command)
                    cursor.close()
                    return f"{old_user_name} has been changed to {new_user_name}"
            else:
                return "You require an admin level account to update a username."

    def delete_user(self, user_name, manager_name, manager_password): # deletes user details
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_admin(manager_name, manager_password):

                with connection.cursor()as cursor:
                  command = f"DELETE FROM `user_info` WHERE `username`= '{user_name}';"
                  cursor.execute(command)
                  cursor.close()
                  return f"{user_name} has been deleted from the database"
            else:
                return "You require an admin level account to delete user details."
