from sql_init import sql_DB
import jwt

class TokenManager():

    def store_token(self, token, username, user_agent):
        db = sqlDB()
        cursor = db.cursor
        command = "INSERT INTO `token_table` (`username`,`user_agent`,`token`) VALUES('{},{},{}')".format(username, user_agent, token)

        cursor.execute(command)
        db.connection.commit()
        #should now have stored username, user_agent, and the token in the appropriate table.
        db.close_down()

        return ("Token stored in database")

    def check_token(self, token, username, user_agent):
        #craft search command
        token_data = jwt.decode(token, 'SECRET_KEY_123456798', 'HS256')
        command = "SELECT * FROM token_table WHERE `token` = {}".format(token)
        #open cursor
        print
        db = sqlDB()
        cursor = db.cursor
        cursor.execute(command)

        db_user_agent = cursor.getColumnIndex('user_agent')
        db_username = cursor.getColumnIndex('username')
        print(db_username)
        print(db_user_agent)
        #Extract token and user value
        if rowcount > 1 and user_agent = db_user_agent and username = db_username
        #rowcount mroe than one

        #username matches
