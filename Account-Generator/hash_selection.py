import hashlib
import bcrypt
import base64
import configparser
from salting import Salting

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from Salt import Salt

class HashSelection():

    def print_hash_options(self):

        return hashlib.algorithms_available


    def read_password_hash_policy(self):
        policy = configparser.ConfigParser()
        policy.read('hash_policy.txt')
        password_hash = policy.get('Policy', 'password_hash').lower()

        return password_hash

    def read_file_hash_policy(self):
        policy = configparser.ConfigParser()
        policy.read('hash_policy.txt')
        password_hash = policy.get('Policy', 'file_hash').lower()

        return password_hash

    def sha1_hash(self, plaintext):
        HF = Salting()
        salt = HF.generate_salt()
        salt_64 = HF.generate_base64_salt(salt)
        saltedpass = salt_64 + plaintext
        return(hashlib.sha1(saltedpass.encode()).hexdigest()), salt_64

    def sha256_hash(self, plaintext):
        HF = Salting()
        salt = HF.generate_salt()
        salt_64 = HF.generate_base64_salt(salt)
        saltedpass = salt_64 + plaintext
        return(hashlib.sha256(saltedpass.encode()).hexdigest()), salt_64

    def sha3_256_hash(self, plaintext):
        HF = Salting()
        salt = HF.generate_salt()
        salt_64 = HF.generate_base64_salt(salt)
        saltedpass = salt_64 + plaintext
        return(hashlib.sha3_256(saltedpass.encode()).hexdigest()), salt_64

    def sha3_512_hash(self, plaintext):
        HF = Salting()
        salt = HF.generate_salt()
        salt_64 = HF.generate_base64_salt(salt)
        saltedpass = salt_64 + plaintext
        return(hashlib.sha3_512(saltedpass.encode()).hexdigest()), salt_64

    def bcrypt_hash(self, plaintext):
        salt = bcrypt.gensalt()
        plainencode = plaintext.encode()
        return(bcrypt.hashpw(plainencode, salt).decode()), salt.decode()
        #return(hashlib.sha3_512(saltedpass.encode()).hexdigest()), salt_64


    # def hash_password(self, password):
    #     HF = Salt()
    #     salt = HF.generate_salt()
    #     salt_64 = HF.generate_base64_salt(salt)
    #     saltedpass = salt_64 + password
    #     hash_type = self.read_password_hash_policy()
    #     return(hashlib.hash_type(saltedpass.encode()).hexdigest()), salt_64
    #     pass
# get the choiceof hash from the hash_policy file and hashes the input with the correct hashing type
# print(HashSelection().print_hash_options())
# print(HashSelection().read_password_hash_policy())
# print(HashSelection().read_file_hash_policy())
# print(HashSelection().sha1_hash("greatpass"))
# print(HashSelection().sha512_256_hash("greatpass"))
# print(HashSelection().bcrypt_hash("greatpass"))
