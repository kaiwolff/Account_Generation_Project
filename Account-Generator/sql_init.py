from mysql.connector import connect, Error

class sql_DB:

    def __init__(self):
        with open("config_sql", "r") as file:
            configs = file.readlines()
            file.close()
        with open(".my_sql_password", "r") as file:
            sqlpassword = file.read().strip()
            file.close()

        self.connection = connect(host=str(configs[0]), user=str(configs[1]).strip(), password=sqlpassword, database="pw_user_db")
        self.cursor = self.connection.cursor()

# print(check_admin("admin", "Lm(6QXlaYsk8"))#Works, returns True if admin details are correct
