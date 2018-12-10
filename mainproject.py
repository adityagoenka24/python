import mysql.connector


class Tinder:
    # This is the constructor
    def __init__(self):
        self.conn = mysql.connector.connect(user="root",password="",host="localhost", database="tinder")
        self.mycursor =self.conn.cursor()
        self.program_menu()

    # Welcome Menu for the user
    def program_menu(self):
        self.program_input=input("""Hey! Welcome to Tinder, What would you want?
        1. Create Account
        2. Login
        3. Exit
        """)
        if self.program_input == "1":
            self.register()
        elif self.program_input == "2":
            self.login()
        else:
            print("\nThanks for using Tinder !!\n")

    def register(self):
        print("Enter the details: ")
        name=input("Name: ")
        email=input("Email: ")
        password=input("Password: ")
        gender = input("Gender: ")
        city = input("City: ")

        # run the insert query

        self.mycursor.execute("""insert into `tinder`.`users`
        (`user_id`,`name`,`email`,`password`,`gender`,`city`) VALUES (NULL,'%s','%s','%s','%s','%s')
        """ %(name,email,password,gender,city))

        self.conn.commit()
        print("Registration successful !! ")
        self.program_menu()

    def login(self):
        email=input("Enter the email: ")
        password = input("Password: ")

        self.mycursor.execute("""select * from `users` where `email` like '%s' and `password` like '%s' """
                              %(email,password))

        user_list = self.mycursor.fetchall()

        count=0;
        for i in user_list:
            count+=1
            current_user = i

        if count == 1:
            print("You have logged in correctly")
            print("Hi ! ",current_user[1])
            self.current_user_id=current_user[0]
            self.user_menu()
        else:
            print("Incorrect Credentials ! ")
            self.program_menu()

    def user_menu(self):
        self.user_choice=input("""What would you like to do?
        1. View All Users
        2. View who proposed you
        3. View your proposals
        4. View matches
        5. Logout
        """)

        if self.user_choice=="1":
            self.view_users()
        elif self.user_choice=="2":
            self.view_user_proposals()
        elif self.user_choice=="3":
            self.view_user_proposed()
        elif self.user_choice=="4":
            self.view_user_matches()
        elif self.user_choice=="5":
            self.user_logout()
        else:
            print("Invalid choice ! Try again ! ")
            self.user_menu()

    def view_users(self):
        print("Following is the user list")
        self.mycursor.execute(""" select * from `users`
        """)
        user_list = self.mycursor.fetchall()
        print("UserID       Name                 Gender                  City")
        for i in user_list:
            print(i[0],"        ",i[1],"          ",i[4],"            ",i[5])

        juliet_id=input("Enter the ID of your juliet: ")
        self.propose(juliet_id)

    def propose(self,juliet_id):
        self.mycursor.execute("""insert into `proposal` (`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL,'%s','%s')
        
        """ %(self.current_user_id,juliet_id))
        self.conn.commit()
        print("Wow! Proposal sent !")
        self.user_menu()

    def view_user_proposals(self):
        print("Users who proposed you: ")
        self.mycursor.execute(""" 
        select * from `proposal` p 
        join `users` u on p.`romeo_id`=u.`user_id` where p.`juliet_id` like '%s'
        """ %(self.current_user_id))

        fan_list=self.mycursor.fetchall()
        print("Here it goes:")
        for i in fan_list:
            print(i[3],"    ",i[4],"      ",i[7],"      ",i[8])

        match=input("Enter the ID of the one you want to propose back (-1 to go back): ")
        if match != "-1":
            self.propose(match)
        else:
            self.user_menu()

    def view_user_proposed(self):
        print("Users who you proposed: ")
        self.mycursor.execute(""" 
                select * from `proposal` p 
                join `users` u on p.`juliet_id`=u.`user_id` where p.`romeo_id` like '%s'
                """ % (self.current_user_id))

        fan_list = self.mycursor.fetchall()
        print("Here it goes:")
        for i in fan_list:
            print(i[3], "    ", i[4], "      ", i[7], "      ", i[8])

        self.user_menu()

    def view_user_matches(self):
        print("Hey ! These are your matches ! ")
        self.mycursor.execute("""
               select * from `proposal` p JOIN 
               `users` u ON p.`juliet_id`=u.`user_id` WHERE 
               `romeo_id` = '%s' and `juliet_id` IN (select `romeo_id` from `proposal` where `juliet_id` like '%s' ) 
        """ %(self.current_user_id,self.current_user_id))
        match_list=self.mycursor.fetchall()
        for i in match_list:
            print(i[3], "    ", i[4], "      ", i[7], "      ", i[8])

        self.user_menu()

    def user_logout(self):
        print("You have successfully logged out")
        self.program_menu()


obj1 = Tinder()


