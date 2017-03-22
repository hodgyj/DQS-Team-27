from tkinter import *
from tkinter import messagebox
import csv

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
        btnCancel = Button(self, text='Cancel', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnCancel.grid(row=3, column=2, sticky=W+E, ipadx=10, padx=10)

def StartWindow():
    root = Tk()
    root.title("Search")
    root.resizable(0,0)
    app = Search(root)
    app.configure(background="white")
    root.mainloop()
    
def input_test(input):
    with open ('tutors.csv','rt') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:

            if input in row[0]:
                searchTut(input)
                break

            else:
                messagebox.showerror("Input Error", "No such ID")
                break
                
def searchTut(id):
    studentList= []
    with open('tutees.csv', 'rt') as csvfile:
        csvReader = csv.reader(csvfile)
        
        for row in csvReader:
            childList =[]
            if id in row[4]:
                childList.append(row[0])

                """Dealing with middle names"""

                if row[3] == "":
                    name = row[1] + ' ' + row[2]
                else:
                    name = row[1] + ' ' + row[3] + " " + row[2]
                    
                childList.append(name)
                studentList.append(childList)
        StartTree(studentList)




"""
Creates a new window, to output the table (should the code below be in a different file?)
"""



class Treelist(Frame):
    # GUI setup
    def __init__(self, master,sList):
        Frame.__init__(self, master)
        self.pack()
        self.list(sList)



    def list(self,sList):
        tree = ttk.Treeview(self)
        tree['show'] = 'headings'
        tree["columns"] = ("one", "two")
        tree.column("one", width=100)
        tree.column("two", width=100)
        tree.heading("one", text="coulmn A")
        tree.heading("two", text="column B")

        for x in sList:
            tree.insert("", 0, text="Line 1", values=(x[0], x[1]))

        tree.pack()

def StartTree(sList):
    root = Tk()
    root.title("TutorList")
    root.resizable(0, 0)
    app = Treelist(root,sList)
    app.configure(background="white")
    root.mainloop()

if __name__ == "__main__":
    import login
