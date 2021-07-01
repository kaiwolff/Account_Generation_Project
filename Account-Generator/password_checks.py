class UserPasswordDetails():

    def check_list(self, password):
    # checks password against passwords in common_passwords.txt. Returns True if password is not in file, False if found.Written by KW
    # sql_password = getpass("Please input your SQL database password: ")
    with connect(host="localhost", user="root", password=sql_password, database="common_password_db") as connection:

        with connection.cursor()as cursor:
            command = "SELECT * FROM `common_passwords` WHERE password = '{}';".format(password)
            cursor.execute(command)
            cursor.fetchall()
            #print(cursor.rowcount)
            #print(password)
            num_occurences = cursor.rowcount
            # print("num_occurences assigned")
            cursor.close()

        if num_occurences > 0:
            return False
        elif num_occurences == 0:
            return True


    def check_policy(self, password):
        # reads password policy, checks if password complies with requirements. Returns True if yes, False if not. Written by KW
        policy_list = self.read_password_policy()
        # print(policy_list)
        # now hav ea list defining password policy
        num_specials = policy_list[0]
        num_lowercase = policy_list[1]
        num_uppercase = policy_list[2]
        num_numbers = policy_list[3]
        min_length = policy_list[4]
        max_length = policy_list[5]
        allowed_specials = policy_list[6]

        count_specials = 0
        count_lower = 0
        count_upper = 0
        count_numbers = 0

        if len(password) < min_length or len(password) > max_length:
            # not compliant if too short or too long
            return False

        for letter in password:
            # check each letter to see if special, lower, upper, or number. Count each of these
            if letter.isdigit():
                count_numbers += 1
            elif letter.isupper():
                count_upper += 1
            elif letter.islower():
                count_lower += 1
            elif letter in allowed_specials:
                count_specials += 1
            else:
                # return false if part of password is not in any allowed category
                print("illegal character")
                return False

        # now have a count of all the lower, upper, special characters and numbers
        if count_upper >= num_uppercase and count_lower >= num_lowercase and count_specials >= num_specials and count_numbers >= num_numbers:
            return True
        else:
            return False


    def check_user_details(self, password, user_firstname, user_lastname, user_birthyear):
        # checks if the password contains the user name or year of birth. Outputs True if no user details in the password. Written by KW
        if user_firstname in password:
            return False
        elif user_lastname in password:
            return False
        elif user_birthyear in password:
            return False
        else:
            return True
