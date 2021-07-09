import hashlib


def hashpass(password, username):
    # encode it to bytes using UTF-8 encoding
    # hash with MD5 (not recommended)
    print("SHA256:", hashlib.sha256(saltpass(username, password)).hexdigest())

def saltpass(username, password):
    salted_pass = username.encode() + password.encode()
    return salted_pass

hashpass("Tyree", "Thisisastrongpass")
