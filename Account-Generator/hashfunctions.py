import hashlib
import string
from password_checks import UserPasswordDetails
import random
import base64
from mysql.connector import connect, Error

with open("config_sql", "r") as file:
    configs = file.readlines()
    file.close()
with open(".my_sql_password", "r") as file:
    sqlpassword = file.read()
    file.close()


class HashFunctions():

    def get_user_pass(self,username):
        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db") as connection:
            with connection.cursor() as cursor:
                command = "SELECT `password` FROM `user_info` WHERE `username` = '{}';".format(username)
                cursor.execute(command)
                password = cursor.fetchone()
                connection.close()
        #print(password[0])
        return password[0]

    def check_pass(self, username, plain_password):
        salt = self.get_user_salt(username)
        check_pass = self.hash_no_salt(plain_password, salt)
        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db") as connection:
            with connection.cursor() as cursor:
                command = "SELECT `password` FROM `user_info` WHERE `username` = '{}';".format(username)
                cursor.execute(command)
                hashed_pass = cursor.fetchone()
                connection.close()
        if check_pass == hashed_pass[0]:
            return True
        else:
            return False
        # print(check_pass)
        # print(hashed_pass)
        # print(salt)



    def get_user_salt(self, username):

        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db") as connection:
            with connection.cursor() as cursor:
                command = "SELECT `Salt` FROM `user_info` WHERE `username` = '{}';".format(username)
                cursor.execute(command)
                salt = cursor.fetchone()
                connection.close()
                return salt[0]

    def hash_no_salt(self, password, salt):
        saltedpass = salt + password
        return hashlib.sha256(saltedpass.encode()).hexdigest()


    def hashpass(self, password):
        # encode it to bytes using UTF-8 encoding
        salt = self.generate_salt()
        salt_64 = self.generate_base64_salt(salt)
        saltedpass = salt_64 + password
        #print(self.hash_no_salt("7$!5I6c2-F1r7m1S", salt_64))
        return (hashlib.sha256(saltedpass.encode()).hexdigest()), salt_64

    # def saltpass(self, password):
    #     salted_pass = self.generate_salt().encode() + password.encode()
    #     return salted_pass

    def generate_salt(self):

        # reading through the password policy and looping through to extract necessary values to check and generates the password
        policy_checklist = UserPasswordDetails().read_salt_policy()
        max_length = sum(policy_checklist)

        # Generating the password using random and string modules
        salt = ""
        for character in range(max_length):

            random_character = random.randint(1,4)

            if random_character == 1:
                salt += random.choice(string.ascii_lowercase)
            elif random_character == 3:
                salt += random.choice(string.ascii_uppercase)
            else:
                salt += random.choice(string.digits)

        return salt

    def generate_base64_salt(self, salt):
        salt_64 = base64.b64encode(salt.encode())
        salt_final = salt_64.decode()
        #print("This is the final salt" + salt_final)
        return salt_final

    # salted_pass = username.encode() + password.encode()
    # b_salt = base64.b64encode(salted_pass)
    # b_message = b_salt.decode('ascii')
    # print(b_message)

# print(HashFunctions().hashpass("7$!5I6c2-F1r7m1S")[0]) # Will return the hashed_value
# print(HashFunctions().hashpass("helloworld")[1]) # Will return the salt
# print(HashFunctions().get_user_salt("User"))
# print(HashFunctions().check_pass("test_username1", "s$Y9h70OXO)nXb7Y"))
# print(HashFunctions().get_user_pass("admin"))
