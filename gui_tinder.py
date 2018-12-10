from tkinter import *
from tinderbackend import *
from tkinter import messagebox

class TinderGUI:
    def __init__(self):

        self.TinderBackend = Tinder()
        self.root= Tk()
        root=Toplevel
        self.root.maxsize(300, 900)

        heading = Label(self.root, text="WELCOME TO TINDER !! ", width=25, height = 3, bg="white",font=("Courier", 16))
        heading.grid(row=0, column=0)

        btnlogin = Button(self.root,text="Login", width=12,height=3,bg="SkyBlue",command=lambda : self.userlogin()).grid(row=2,column=0,padx=30,pady=10)
        btnRegister = Button(self.root, text="Register", width=12, height=3, bg="SkyBlue",command=lambda : self.userregister()).grid(row=3, column=0, padx=30,
                                                                                          pady=10)

        btnExit = Button(self.root, text="Exit", width=12, height=3, bg="SkyBlue", command=self.root.destroy).grid(row=4, column=0,
                                                                                                padx=30,
                                                                                                pady=10)
        self.root.mainloop()

    def userlogin(self):
        child = Toplevel(master=self.root)
        child.maxsize(500, 900)
        child.title("Login")
        emaillabel = Label(child, text="Email ", width=10, height=1, font=("Courier", 16))
        emaillabel.grid(row=0,column=0)
        email=Entry(child, width=20, bg="white",font=("Courier", 16))
        email.grid(row=0, column=2)
        label = Label(child, text="Password ", width=10, height=1, font=("Courier", 16))
        label.grid(row=1, column=0)
        password = Entry(child, width=20, bg="white", font=("Courier", 16), show="*")
        password.grid(row=1, column=2)

        submit = Button(child,width=20,bg="SkyBlue", text="Login", command=lambda :self.verify(child,email.get(),password.get()))
        submit.grid(row=2, column=2)

    def verify(self,child,useremail,userkey):
        flag = self.TinderBackend.login(useremail,userkey)
        if flag == 1:
            messagebox.showinfo("Success", "Successfully Logged In")
            child.destroy()
        else:
            messagebox.showinfo("Invalid", "Wrong Credentials")


    def userregister(self):
        child = Toplevel(master=self.root)
        child.maxsize(500, 900)
        child.title("Register")
        emaillabel = Label(child, text="Email ", width=10, height=1, font=("Courier", 16))
        emaillabel.grid(row=0, column=0)
        email = Entry(child, width=20, bg="white", font=("Courier", 16))
        email.grid(row=0, column=2)
        label = Label(child, text="Password ", width=10, height=1, font=("Courier", 16))
        label.grid(row=1, column=0)
        password = Entry(child, width=20, bg="white", font=("Courier", 16), show="*")
        password.grid(row=1, column=2)
        namelabel = Label(child, text="Name ", width=10, height=1, font=("Courier", 16))
        namelabel.grid(row=2, column=0)
        name = Entry(child, width=20, bg="white", font=("Courier", 16))
        name.grid(row=2, column=2)
        genderlabel = Label(child, text="Gender ", width=10, height=1, font=("Courier", 16))
        genderlabel.grid(row=3, column=0)
        gender = Entry(child, width=20, bg="white", font=("Courier", 16))
        gender.grid(row=3, column=2)
        citylabel = Label(child, text="City ", width=10, height=1, font=("Courier", 16))
        citylabel.grid(row=4, column=0)
        city = Entry(child, width=20, bg="white", font=("Courier", 16))
        city.grid(row=4, column=2)

        submit = Button(child, width=20, bg="SkyBlue", text="Register",
                        command=lambda: self.senddetails(child, email.get(), password.get(),name.get(),gender.get(),city.get()))
        submit.grid(row=5, column=2)


    def senddetails(self,child,useremail,userkey,name,gender,city):
        flag = self.TinderBackend.register(useremail,userkey,name,gender,city)
        messagebox.showinfo("Success", "Successfully Registered")
        child.destroy()





obj1 = TinderGUI()