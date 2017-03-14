from tkinter import *
from PIL import Image, ImageTk

class Search(Frame):
    # GUI setup
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createButtons()

    def createTitle(self):
        lblTitle = Label(self, text='Search', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=5, sticky=W+E, pady=10, padx=20)

    def createButtons(self):
        btnTutor = Button(self, text='Tutor', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnTutor.grid(row=1, column=1, sticky=W+E, ipadx=40)

        btnTutee = Button(self, text='Tutee', font=('Segoe UI', 16), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnTutee.grid(row=1, column=3, sticky=W+E, ipadx=40)

        # Add spacing to the columns and bottom row
        self.columnconfigure(0, minsize=20)
        self.columnconfigure(2, minsize=20)
        self.columnconfigure(4, minsize=20)

        self.rowconfigure(2, minsize=15)
        

root = Tk()
root.title("Search")
root.resizable(0,0)
app = Search(root)
app.configure(background="white")
root.mainloop()