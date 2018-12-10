import mysql.connector


class Tinder:
    # This is the constructor
    def __init__(self):
        self.conn = mysql.connector.connect(user="root",password="",host="localhost", database="tinder")
        self.mycursor =self.conn.cursor()

    def login(self,em,key):
        email=em
        password = key

        self.mycursor.execute("""select * from `users` where `email` like '%s' and `password` like '%s' """
                              %(email,password))

        user_list = self.mycursor.fetchall()

        count=0;
        for i in user_list:
            count+=1
            current_user = i
        flag = 0
        if count == 1:
            print("You have logged in correctly")
            flag = 1
            self.current_user_id=current_user[0]

        return flag


    def register(self,email,password,name,gender,city):

        # run the insert query

        self.mycursor.execute("""insert into `tinder`.`users`
        (`user_id`,`name`,`email`,`password`,`gender`,`city`) VALUES (NULL,'%s','%s','%s','%s','%s')
        """ %(name,email,password,gender,city))

        self.conn.commit()
