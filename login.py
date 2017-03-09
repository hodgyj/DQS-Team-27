from tkinter import *


class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.createInputs()
        self.createButton()
        self.createTitle()


    def createInputs(self):
            Userin = Entry(self)
            Userin.grid(row=2, column=5)
            #Userin.pack(side='top')

            Passin = Entry(self,show = "*")
            Passin.grid(row=4, column=5)


    def createButton(self):
            Submit = Button(self, text='Login',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT)
            Submit.grid(row =5,column = 5)

    def createTitle(self):
            lblTitle = Label(self, text='T&T Systems™', font=('Segoe UI Light', 32))
            lblTitle.grid(row=0, column=4, columnspan=7, sticky=W + E,pady =4)

            User = Label(self, text= 'Username',font=('Segoe UI light', 14))
            User.grid(row=1, column =4,columnspan = 1)

            Pass = Label(self, text= 'Password',font=('Segoe UI light', 14))
            Pass.grid(row = 3, column = 4,columnspan = 1)


root = Tk()
root.title("T&T")
root.resizable(0,0)
app = Login(root)
app.pack(side="top", fill="both", expand=True)
root.wm_geometry("290x200")
root.mainloop()