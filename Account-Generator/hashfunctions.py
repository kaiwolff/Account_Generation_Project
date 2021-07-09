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

    def get_user_salt(self, username):

        with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db") as connection:
            with connection.cursor() as cursor:
                command = "SELECT 'Salt' FROM `user_info` WHERE `username`= '{}';".format(username)
                cursor.execute(command)
                num_occurences = cursor.rowcount
                print(num_occurences)
                # for salt in cursor:
                #     print(salt)
                # salt = cursor.fetchone()
                #
                # return salt
#try the for loop
#still prints none
# functions
    # def validate_user(username, password):
    #     with connect(host=str(configs[0]), user=str(configs[1]), password=sqlpassword, database="pw_user_db") as connection:
    #         with connection.cursor() as cursor:
    #             command = "SELECT * FROM `user_info` WHERE `username`= '{}' AND `password`='{}';".format(
    #                 user_name,  user_password)
    #
    #             cursor.execute(command)


    def hashpass(self, password):
        # encode it to bytes using UTF-8 encoding
        salt = self.generate_salt()
        salt_64 = self.generate_base64_salt(salt)
        saltedpass = salt_64 + password
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
        salt_final = salt_64.decode('ascii')
        return salt_final

    # salted_pass = username.encode() + password.encode()
    # b_salt = base64.b64encode(salted_pass)
    # b_message = b_salt.decode('ascii')
    # print(b_message)

# print(HashFunctions().hashpass("helloworld")[0])
# print(HashFunctions().hashpass("helloworld")[1])
print(HashFunctions().get_user_salt("test_firstname"))
