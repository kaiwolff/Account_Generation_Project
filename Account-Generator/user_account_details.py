from mysql.connector import connect, Error
from password_checks import UserPasswordDetails
import hashlib
from hashfunctions import HashFunctions

with open("config_sql", "r") as file:
    configs = file.readlines()
    file.close()
with open(".my_sql_password", "r") as file:
    sqlpassword = file.read()
    file.close()

class UserAccountDetails():
    # pw_user_db, user_info, username, FirstName, LastName, BirthYear, password, Manager
    # host=configs[0]52.214.153.42

    def user_login(self, username, password):
        if self.check_existence(username):
            if HashFunctions().check_pass(username, password):
                return True # change it to return a JSON token
            else:
                return False # Wrong password
        else:
            return False # Wrong username



    def check_admin(self, user_name, user_password):  # check if the admin value is true

        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db") as connection:
            with connection.cursor() as cursor:
                # NEED TO RETRIEVE SALT, THEN HASH AND CHECK FOR CORRECT PASSWORDS
                command = "SELECT * FROM `user_info` WHERE `username`= '{}' AND `password`='{}' AND `Manager` = 1;".format(
                    user_name,  HashFunctions().get_user_pass(user_name))

                cursor.execute(command)
                #connection.commit()
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()
                # print(HashFunctions().get_user_pass(user_name))
                if num_occurences > 0:
                    return True
                elif num_occurences == 0:
                    return False

    def check_existence(self, user_name):  # checks if a user exists in a database

        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword,
                     database="pw_user_db") as connection:
            with connection.cursor()as cursor:
                command = "SELECT * FROM `user_info` WHERE `username`= '{}';".format(user_name)
                cursor.execute(command)
                # connection.commit()
                cursor.fetchall()
                num_occurences = cursor.rowcount
                # print("num_occurences assigned")
                cursor.close()

                if num_occurences > 0:
                    return True  # if it exists it will return True
                else:
                    return False  # if doesnt exists will return False

    def create_new_user(self, user_name, first_name, last_name, birth_year, password):  # creates user details
        # check_admin()
        # birth_year = int(birth_year)

        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword,
                     database="pw_user_db") as connection:

            if self.check_existence(user_name):
                return "{} already exists.".format(user_name)

            elif not UserPasswordDetails().check_list(password) or not UserPasswordDetails().check_policy(
                    password) or not UserPasswordDetails().check_user_details(first_name, last_name, birth_year,
                                                                              password):
                password = UserPasswordDetails().generate_password()
                with connection.cursor()as cursor:
                    return "Your password is weak. How about {}".format(password)

            else:
                list = HashFunctions().hashpass(password)
                with connection.cursor()as cursor:
                    #INSERT INTO `user_info`(`Key`, `username`, `FirstName`, `LastName`, `BirthYear`, `password`, `Manager`, `Salt`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]')
                    command = "INSERT INTO `user_info`(`username`, `FirstName`, `LastName`, `BirthYear`, `password`, `Manager`, `Salt`) VALUES ('{}', '{}', '{}', '{}', '{}', NULL, '{}');".format(
                        user_name, first_name, last_name, birth_year, list[0], list[1])
                    cursor.execute(command)
                    connection.commit()
                    cursor.close()
                    list = []
                    return "You have been successfully added to the database system."

    def change_to_manager(self, user_name, manager_name, manager_password):  # changes the value of user role back to manager role
        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword,
                     database="pw_user_db") as connection:

            if self.check_admin(manager_name, manager_password):
                if self.check_existence(user_name):
                    with connection.cursor()as cursor:
                        command = "UPDATE `user_info` SET `Manager`= '1' WHERE `username` = '{}';".format(user_name)
                        cursor.execute(command)
                        connection.commit()
                        cursor.close()
                        return "The account has been changed to admin status."
                else:
                    return "The user doesn't exist"
            else:
                return "You require an admin level account to change from user to admin status."

    def change_to_user(self, user_name, manager_name, manager_password):  # changes the value of manager role back to user role
        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword,
                     database="pw_user_db") as connection:

            if self.check_admin(manager_name, manager_password):
                if self.check_existence(user_name):
                    with connection.cursor()as cursor:
                        command = "UPDATE `user_info` SET `Manager`=NULL WHERE `username` = '{}';".format(user_name)
                        cursor.execute(command)
                        connection.commit()
                        cursor.close()
                        return "The account has been changed to user"
                else:
                    return "The user doesn't exist"
            else:
                return "You require an admin level account to update user status."


    def change_username(self, old_user_name, new_user_name, manager_name,
                        manager_password):  # only if the user is an admin, allows to change the user name
        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword,
                     database="pw_user_db") as connection:
            if self.check_admin(manager_name, manager_password):
                if self.check_existence(old_user_name):
                    if not self.check_existence(new_user_name):
                        with connection.cursor()as cursor:

                            command = "UPDATE `user_info` SET `username` = '{}' WHERE `username` = '{}';".format(
                                new_user_name, old_user_name)
                            cursor.execute(command)
                            connection.commit()
                            cursor.close()
                            return "{} has been changed to {}".format(old_user_name, new_user_name)
                    else:
                        return "The new user already exists in the database"
                else:
                    return "The user doesn't exist"
            else:
                return "You require an admin level account to update a username."


    def delete_user(self, user_name, manager_name, manager_password):  # deletes user details
        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword,
                     database="pw_user_db") as connection:

            if self.check_admin(manager_name, manager_password):
                if self.check_existence(user_name):
                    with connection.cursor()as cursor:
                        command = "DELETE FROM `user_info` WHERE `username`= '{}';".format(user_name)
                        cursor.execute(command)
                        connection.commit()
                        cursor.close()
                        return "The account {} has been deleted from the database".format(user_name)
                else:
                    return "The user you are trying to delete isn't on the database"
            else:
                return "You require an admin level account to delete user details."

# File Test

# print(UserAccountDetails().delete_user("Afshana_username", "admin", "Lm(6QXlaYsk8")) #Works, Used a test DB to delete an entry
# print(UserAccountDetails().change_to_user("admin", "admin", "Lm(6QXlaYsk8")) #Works, returns the right strings depends on the input
# print(UserAccountDetails().create_new_user("admin","admin_firstname","admin_lastname", "1997", "Lm(6QXlaYsk8")) #Works, if accort already exists will infom user, if password is weak will generate new pass inserts to DB
# print(UserAccountDetails().check_admin("admin", "Lm(6QXlaYsk8"))#Works, returns True if admin details are correct
# print(UserAccountDetails().change_username("test_user", "New_user", "admin", "admin"))#Works, doesnt let the new username change if it's already in uses, only lets you change name if you have admin details
# print(UserAccountDetails().change_to_manager("admin", "admin", "Lm(6QXlaYsk8"))#Works, Only works if you have admin details and the username is in the database
# print(UserAccountDetails().check_existence("admin"))#Works, Check is a username is in teh database
# print(UserAccountDetails().user_login("test_username1","7$!5I6c2-F1r7m1S"))
