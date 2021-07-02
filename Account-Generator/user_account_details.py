from mysql.connector import connect, Error
from password_checks import UserPasswordDetails

class UserAccountDetails():
    # pw_user_db, user_info, username, FirstName, LastName, BirthYear, password, Manager

    def check_admin(self, user_name, user_password): # check if the admin value is true

        with connect(host = "localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            with connection.cursor() as cursor:

                command = "SELECT * FROM `user_info` WHERE `username`= '{}' AND `password`='{}' AND `Manager` = 1;".format(user_name, user_password)

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
                command = "SELECT * FROM `user_info` WHERE `username`= '{}';".format(user_name)
                cursor.execute(command)
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()

                if num_occurences > 0:
                    return True
                elif num_occurences == 0:
                    return False


    def create_new_user(self, user_name, first_name, last_name, birth_year, password): # creates user details
        #check_admin()
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_existence(user_name):
                return "{} already exists.".format(user_name)


            elif UserPasswordDetails.check_list(password) or UserPasswordDetails.check_policy(password) or UserPasswordDetails.check_user_details(password, first_name, last_name, birth_year):
                password = UserPasswordDetails.generate_password()
                with connection.cursor()as cursor:
                    command = "INSERT INTO `user_info` (username, FirstName, LastName, password, BirthYear, Manager) VALUES ('{}, '{}', '{}', '{}', '{}', '0');".format(user_name, first_name, last_name, password, birth_year)
                    cursor.execute(command)
                    cursor.close()
                return "Your password is weak."

            else:
                with connection.cursor()as cursor:
                    command = "INSERT INTO `user_info` (username, FirstName, LastName, password, BirthYear, Manager) VALUES ('{}', '{}', '{}', '{}', '{}','0');".format(user_name, first_name, last_name, password, birth_year)
                    cursor.execute(command)
                    cursor.close()
                    return "You have been successfully added to the database system."



    def change_to_manager(self, user_name, manager_name, manager_password): # changes the value of user role back to manager role
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_admin(manager_name, manager_password):
                with connection.cursor()as cursor:
                    command = "UPDATE `user_info` SET `Manager`= 1 WHERE `username` = '{}';".format(user_name)
                    cursor.execute(command)
                    cursor.close()
                    return "The account has been changed to admin status."

            else:
                return "You require an admin level account to change from user to admin status."


    def change_to_user(self, user_name, manager_name, manager_password): # changes the value of manager role back to user role
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_admin(manager_name, manager_password):
                with connection.cursor()as cursor:
                    command = "UPDATE `user_info` SET `Manager` = 0 WHERE `username` = '{user_name}';".format(user_name)

                    cursor.execute(command)
                    cursor.close()
                    return "The account has been changed to user"

            else:
                return "You require an admin level account to update user status."


    def change_username(self, old_user_name, new_user_name, manager_name, manager_password): # only if the user is an admin, allows to change the user name
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:
            if check_admin(manager_name, manager_password):

                with connection.cursor()as cursor:

                    command = "UPDATE `user_info` SET `username` = '{}' WHERE `username` = '{}';".format(new_user_name, old_user_name)
                    cursor.execute(command)
                    cursor.close()
                    return "{} has been changed to {}".format(old_user_name, new_user_name)

            else:
                return "You require an admin level account to update a username."


    def delete_user(self, user_name, manager_name, manager_password): # deletes user details
        with connect(host="localhost", user="root", password="my_secret_password", database="pw_user_db") as connection:

            if check_admin(manager_name, manager_password):

                with connection.cursor()as cursor:
                  command = "DELETE FROM `user_info` WHERE `username`= '{}';".format(user_name)
                  cursor.execute(command)
                  cursor.close()
                  return "The account {} has been deleted from the database".format(user_name)
            else:
                return "You require an admin level account to delete user details."
