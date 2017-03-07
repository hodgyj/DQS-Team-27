from tkinter import *

class Questionnaire(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def createTitle(self):
        lblTitle = Label(self, text='Cool Program', font=('MS', 32, 'bold'))
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=10, padx=10)
        # lblProg = Label(self, text='Degree Programme: ', font=('Comic Sans MS',16,'bold'))
        # lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)
    def createButtons(self):
        btnAssign = Button(self, text='Assign', font=('MS', 16))
        btnAssign.grid(row=1, column=1, columnspan=2, sticky=W+E)
        btnReassign = Button(self, text='Reassign', font=('MS', 14))
        btnReassign.grid(row=2, column=1, columnspan=2, sticky=W+E)


        btnSearch = Button(self, text='Search', font=('MS', 12))
        btnSearch.grid(row=3, column=0)
        btnQuota = Button(self, text='Quotas', font=('MS', 12))
        btnQuota.grid(row=3, column=3)

root = Tk()
root.title("Teamwork Questionnaire")
app = Questionnaire(root)
root.mainloop()