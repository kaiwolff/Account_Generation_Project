import hashlib
import string
from password_checks import UserPasswordDetails
import random
import base64

class HashFunctions():

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
        #print(password) testing
        # print(f"this is the salt:{salt}")
        # salt_64 = base64.b64encode(salt.encode())
        # salt = salt_64.decode('ascii')
        return salt

    def generate_base64_salt(self, salt):
        salt_64 = base64.b64encode(salt.encode())
        salt_final = salt_64.decode('ascii')
        return salt_final

    # salted_pass = username.encode() + password.encode()
    # b_salt = base64.b64encode(salted_pass)
    # b_message = b_salt.decode('ascii')
    # print(b_message)

print(HashFunctions().hashpass("helloworld"))
