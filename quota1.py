from tkinter import *

class Quota(Frame):
  
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def createTitle(self):
        title = Label(self, text='Tutor Quotas', font=('Segoe UI Light', 32), background="white")
       	title.grid(row=0, column=0, columnspan=5, pady=10, padx=20)

    def createButtons(self):
        btnAssign = Button(self, text='Display', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnAssign.grid(row=1, column=1, columnspan=3, pady=20, padx=20)

root = Tk()
root.title("Quota")
app = Quota(root)
app.configure(background="white")
root.mainloop()