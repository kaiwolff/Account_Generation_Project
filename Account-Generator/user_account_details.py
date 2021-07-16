from mysql.connector import connect, Error
from password_checks import UserPasswordDetails
import hashlib
from sql_init import sql_DB
from hashfunctions import HashFunctions

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

        command = "SELECT * FROM `user_info` WHERE `username`= '{}' AND `password`='{}' AND `Manager` = 1;".format(
            user_name,  HashFunctions().get_user_pass(user_name))
        db = sql_DB()
        cursor = db.cursor
        cursor.execute(command)
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

        db = sql_DB()
        cursor = db.cursor
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
        db = sql_DB()
        cursor = db.cursor

        if self.check_existence(user_name):
            return "{} already exists.".format(user_name)

        elif not UserPasswordDetails().check_list(password) or not UserPasswordDetails().check_policy(
                password) or not UserPasswordDetails().check_user_details(first_name, last_name, birth_year,
                                                                          password):
            password = UserPasswordDetails().generate_password()

            return "Your password is weak. How about {}".format(password)

        else:
            list = HashFunctions().hashpass(password)
            #INSERT INTO `user_info`(`Key`, `username`, `FirstName`, `LastName`, `BirthYear`, `password`, `Manager`, `Salt`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]')
            command = "INSERT INTO `user_info`(`username`, `FirstName`, `LastName`, `BirthYear`, `password`, `Manager`, `Salt`) VALUES ('{}', '{}', '{}', '{}', '{}', NULL, '{}');".format(
                user_name, first_name, last_name, birth_year, list[0], list[1])
            cursor.execute(command)
            db.connection.commit()
            cursor.close()
            list = []
            return "You have been successfully added to the database system."

    def change_to_manager(self, user_name, manager_name, manager_password):  # changes the value of user role back to manager role
        db = sql_DB()
        cursor = db.cursor

        if self.check_admin(manager_name, manager_password):
            if self.check_existence(user_name):
                command = "UPDATE `user_info` SET `Manager`= '1' WHERE `username` = '{}';".format(user_name)
                cursor.execute(command)
                db.connection.commit()
                cursor.close()
                return "The account has been changed to admin status."
            else:
                return "The user doesn't exist"
        else:
            return "You require an admin level account to change from user to admin status."

    def change_to_user(self, user_name, manager_name, manager_password):  # changes the value of manager role back to user role
        db = sql_DB()
        cursor = db.cursor
        if self.check_admin(manager_name, manager_password):
            if self.check_existence(user_name):
                command = "UPDATE `user_info` SET `Manager`=NULL WHERE `username` = '{}';".format(user_name)
                cursor.execute(command)
                db.connection.commit()
                cursor.close()
                return "The account has been changed to user"
            else:
                return "The user doesn't exist"
        else:
            return "You require an admin level account to update user status."


    def change_username(self, old_user_name, new_user_name, manager_name,
                        manager_password):  # only if the user is an admin, allows to change the user name
        db = sql_DB()
        cursor = db.cursor
        if self.check_admin(manager_name, manager_password):
            if self.check_existence(old_user_name):
                if not self.check_existence(new_user_name):
                    command = "UPDATE `user_info` SET `username` = '{}' WHERE `username` = '{}';".format(
                        new_user_name, old_user_name)
                    cursor.execute(command)
                    db.connection.commit()
                    cursor.close()
                    return "{} has been changed to {}".format(old_user_name, new_user_name)
                else:
                    return "The new user already exists in the database"
            else:
                return "The user doesn't exist"
        else:
            return "You require an admin level account to update a username."


    def delete_user(self, user_name, manager_name, manager_password):  # deletes user details
        db = sql_DB()
        cursor = db.cursor
        if self.check_admin(manager_name, manager_password):
            if self.check_existence(user_name):
                command = "DELETE FROM `user_info` WHERE `username`= '{}';".format(user_name)
                cursor.execute(command)
                db.connection.commit()
                cursor.close()
                return "The account {} has been deleted from the database".format(user_name)
            else:
                return "The user you are trying to delete isn't on the database"
        else:
            return "You require an admin level account to delete user details."

# File Test

#print(UserAccountDetails().delete_user("TestUser97", "adin", "Lm(6QXlaYsk8")) #Works, Used a test DB to delete an entry
# print(UserAccountDetails().change_to_user("admin", "admin", "Lm(6QXlaYsk8")) #Works, returns the right strings depends on the input
print(UserAccountDetails().create_new_user("TestUser", "test_first", "test_last", "1990", "YVW-5DMBUvTJfJ")) #Works, if accort already exists will infom user, if password is weak will generate new pass inserts to DB
# print(UserAccountDetails().check_admin("admin", "Lm(6QXlaYsk8"))#Works, returns True if admin details are correct
print(UserAccountDetails().change_username("TestUser", "admin", "admin", "admin"))#Works, doesnt let the new username change if it's already in uses, only lets you change name if you have admin details
# print(UserAccountDetails().change_to_manager("admin", "admin", "Lm(6QXlaYsk8"))#Works, Only works if you have admin details and the username is in the database
# print(UserAccountDetails().check_existence("admin"))#Works, Check is a username is in teh database
# print(UserAccountDetails().user_login("TestUser","SPKNEZGM+hC9kS"))
