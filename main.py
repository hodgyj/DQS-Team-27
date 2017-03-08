from tkinter import *

class MainMenu(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def createTitle(self):
        lblTitle = Label(self, text='Cool Program', font=('MS', 32, 'bold'))
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=10, padx=10)

    def createButtons(self):
        btnAssign = Button(self, text='Assign', font=('MS', 16), background='#E91E63', foreground='#FFFFFF')
        btnAssign.grid(row=1, column=1, columnspan=2, sticky=W+E, ipady=10, ipadx=30)
        btnReassign = Button(self, text='Reassign', font=('MS', 12))
        btnReassign.grid(row=2, column=1, columnspan=2, sticky=W+E)

        btnSearchTutors = Button(self, text='Search', font=('MS', 12))
        btnSearchTutors.grid(row=3, column=0, pady=10)
        btnQuota = Button(self, text='Quotas', font=('MS', 12))
        btnQuota.grid(row=3, column=3)

root = Tk()
root.title("Amazing")
root.resizable(0,0)
app = MainMenu(root)
root.mainloop()