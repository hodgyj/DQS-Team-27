from tkinter import *
from PIL import Image, ImageTk

class MainMenu(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def openAssign(self):
        import assign
        assign.StartWindow()
    
    def openReassign(self):
        import reassign
        reassign.StartWindow()

    def openSearch(self):
        import search
        search.StartWindow()

    def openQuota(self):
        import quota1
        quota1.StartWindow()
    

    def createTitle(self):
        lblTitle = Label(self, text='T&T Systems™', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E, pady=10, padx=20)

    def createButtons(self):
        btnAssign = Button(self, text='Assign', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF', command=self.openAssign)
        btnAssign.grid(row=1, column=1, columnspan=2, sticky=W+E, ipadx=40)
        btnReassign = Button(self, text='Reassign', font=('Segoe UI', 12), command=self.openReassign)
        btnReassign.grid(row=2, column=1, columnspan=2, sticky=W+E)

        btnSearch = Button(self, text='Search', font=('Segoe UI', 12), compound=LEFT, command=self.openSearch)
        btnSearch.grid(row=3, column=0, pady=10)
        btnQuota = Button(self, text='Quotas', font=('Segoe UI', 12), command=self.openQuota)
        btnQuota.grid(row=3, column=3)

def StartWindow():
    root = Tk()
    root.title("Tutor & Tutee")
    root.resizable(0,0)
    app = MainMenu(root)
    app.configure(background="white")
    root.mainloop()

if __name__ == "__main__":
    import login