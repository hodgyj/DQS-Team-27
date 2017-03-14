from tkinter import *
from PIL import Image, ImageTk

class Search(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createInput()

    def createTitle(self):
        lblTitle = Label(self, text='Tutee Search', font=('Segoe UI Light', 32))
        lblTitle.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=5, padx=20)

    def createInput(self):
        lblHelp = Label(self, text='Please enter the tutee student number:', font=('Segoe UI Light', 16))
        lblHelp.grid(row=1, column=0, columnspan=3, sticky=W+E)

        txtSearch = Entry(self, font=('Segoe UI Light', 16), foreground="#2196F3")
        txtSearch.grid(row=2, column=1, sticky=W+E, ipadx=20)

        btnSearch = Button(self, text='Search', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnSearch.grid(row=3, column=0, sticky=W+E, ipadx=10, pady=15, padx=10)
        btnCancel = Button(self, text='Cancel', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnCancel.grid(row=3, column=2, sticky=W+E, ipadx=10, padx=10)

        
        

root = Tk()
root.title("Search")
root.resizable(0,0)
app = Search(root)
root.mainloop()