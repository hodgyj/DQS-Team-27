from tkinter import *
from tkinter import messagebox
import csv
from sys import exit

class Search(Frame):
    # GUI setup

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createInput()



    def createTitle(self):
        lblTitle = Label(self, text='Tutor Search', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=5, padx=20)

    def createInput(self):
        lblHelp = Label(self, text='Please enter the tutor ID:', font=('Segoe UI Light', 16), background="white")
        lblHelp.grid(row=1, column=0, columnspan=3, sticky=W+E)

        txtSearch = Entry(self, font=('Segoe UI Light', 16), foreground="#2196F3", background="white")
        txtSearch.grid(row=2, column=1, sticky=W+E, ipadx=20)



        btnSearch = Button(self, text='Search', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF',
                           foreground='#FFFFFF', command = lambda: input_test(txtSearch.get()))
        btnSearch.grid(row=3, column=0, sticky=W+E, ipadx=10, pady=15, padx=10)
        btnCancel = Button(self, text='Cancel', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6',
                           activeforeground='#FFFFFF', foreground='#FFFFFF',command = lambda: exit()) #in future, return to previous screen
        btnCancel.grid(row=3, column=2, sticky=W+E, ipadx=10, padx=10)




def Start_Window():
    root = Tk()
    root.title("Search")
    root.resizable(0,0)
    app = Search(root)
    app.configure(background="white")
    root.mainloop()

def input_test(input):

    with open ('TutorID.csv','rt') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:

            if input in row[0]:
                SearchTut(input)
                break

            else:
                messagebox.showerror("Input Error", "No such ID")
                break



def SearchTut(id):
    Tuteelist =[]
    Tutorlist = []
    """
    Dunno how the groups.csv file look atm, so give it a shot when i find out

    with open(groups.csv) as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
    """




Start_Window()



