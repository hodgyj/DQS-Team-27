from tkinter import *


class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createTitle()
        self.createInputs()
        self.createButton()


    def createTitle(self):
            lblTitle = Label(self, text='T&T Systems™', font=('Segoe UI Light', 32))
            lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E)

    def createInputs(self):      
            lblUser = Label(self, text='Username:', font=('Segoe UI Light', 18))
            lblUser.grid(row=1, column=0, columnspan=3, sticky=W+E)

            lblPass = Label(self, text='Password:', font=('Segoe UI Light', 18))
            lblPass.grid(row=3, column=0, columnspan=3, sticky=W+E)

            txtUser = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
            txtUser.grid(row=2, column=0, columnspan=3, sticky=W+E, padx=20)

            txtPass = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white', show = "*")
            txtPass.grid(row=4, column=0, columnspan=3, sticky=W+E, padx=20)

    def createButton(self):
            btnSubmit = Button(self, text='Login',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT)
            btnSubmit.grid(row=6, column=1, pady=10, ipadx=2)

root = Tk()
root.title("T&T")
root.resizable(0,0)
app = Login(root)
root.mainloop()