from tkinter import *
from PIL import Image, ImageTk

class MainMenu(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def createTitle(self):
        lblTitle = Label(self, text='T&T Systems™', font=('Segoe UI Light', 32))
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=10, padx=20)

    def createButtons(self):
        btnAssign = Button(self, text='Assign', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnAssign.grid(row=1, column=1, columnspan=2, sticky=W+E, ipady=10, ipadx=30)
        btnReassign = Button(self, text='Reassign', font=('Segoe UI', 12))
        btnReassign.grid(row=2, column=1, columnspan=2, sticky=W+E)

        btnSearchTutors = Button(self, text='Search', font=('Segoe UI', 12), compound=LEFT)
        btnSearchTutors.grid(row=3, column=0, pady=10)
        btnQuota = Button(self, text='Quotas', font=('Segoe UI', 12))
        btnQuota.grid(row=3, column=3)

root = Tk()
root.title("Tutor & Tutee")
root.resizable(0,0)
app = MainMenu(root)
root.mainloop()