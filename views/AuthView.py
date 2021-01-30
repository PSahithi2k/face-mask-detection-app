from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers.AuthController import AuthController

class AuthView:

    def load(self):
        self.window = Tk()
        self.window.title("cheating detection application")

        tab_control = ttk.Notebook(self.window)

        login_frame = Frame(tab_control, bg='white', padx=20, pady=20)
        register_frame = Frame(tab_control, bg='white', padx=20, pady=20)

        tab_control.add(login_frame, text='Login')
        tab_control.add(register_frame, text='Register')

        self.login(login_frame)
        self.register(register_frame)

        tab_control.grid()

        self.window.mainloop() 

    def login(self, login_frame):

        #create user_name lable and entry
        username_lable = Label(login_frame,text='username')
        username_lable.grid(row=0, column=0)

        username_entry = Entry(login_frame, width=20)
        username_entry.grid(row=0, column=1)

        #create password lable and extry
        password_lable = Label(login_frame, text='password')
        password_lable.grid(row=1, column=0)

        password_entry = Entry(login_frame, show='*', width=20)
        password_entry.grid(row=1, column=1)


        #create button for login
        login_button = Button(login_frame, text='Login',  command= lambda: self.login_control(username_entry.get(), password_entry.get()), padx=5, pady=5)
        login_button.grid(row=2, column=1, pady=5)

    def register(self, register_frame):

        window = register_frame

        name_lable = Label(window,text='name')
        name_lable.grid(row=0, column=0)

        name_entry = Entry(window, width=20)
        name_entry.grid(row=0, column=1)

        username_lable = Label(window,text='username')
        username_lable.grid(row=1, column=0)

        username_entry = Entry(window, width=20)
        username_entry.grid(row=1, column=1)

        password_lable = Label(window, text='password')
        password_lable.grid(row=2, column=0)

        password_entry = Entry(window, show='*', width=20)
        password_entry.grid(row=2, column=1)

        email_lable = Label(window,text='email')
        email_lable.grid(row=3, column=0)

        email_entry = Entry(window, width=20)
        email_entry.grid(row=3, column=1)

        phone_lable = Label(window,text='phone')
        phone_lable.grid(row=4, column=0)

        phone_entry = Entry(window, width=20)
        phone_entry.grid(row=4, column=1)

        login_button = Button(window, text='Register',  command= lambda: self.register_control(name_entry.get(), phone_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()), padx=5, pady=5)
        login_button.grid(row=5, column=1, pady=5)

    def login_control(self, username, password):
        ac = AuthController()
        message = ac.login(username, password)

        if(message == 1):
            self.window.destroy()
            self.transfer_control()
        else:
            messagebox.showinfo('Information', message)


    def register_control(self, name, phone, email, username, password):
        ac = AuthController()
        message = ac.register(name, phone, email, username, password)
        messagebox.showinfo('Information', message)



if __name__ == '__main__':
    av = AuthView()




