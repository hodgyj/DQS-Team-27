from tkinter import *
from tkinter import messagebox,ttk
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
        lblTitle.grid(row=0, column=0, columnspan=3, sticky=W + E, pady=5, padx=20)

    def createInput(self):
        lblHelp = Label(self, text='Please enter the tutor ID:', font=('Segoe UI Light', 16), background="white")
        lblHelp.grid(row=1, column=0, columnspan=3, sticky=W + E)

        txtSearch = Entry(self, font=('Segoe UI Light', 16), foreground="#2196F3", background="white")
        txtSearch.grid(row=2, column=1, sticky=W + E, ipadx=20)

        btnSearch = Button(self, text='Search', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6',
                           activeforeground='#FFFFFF',
                           foreground='#FFFFFF', command=lambda: input_test(txtSearch.get()))
        btnSearch.grid(row=3, column=0, sticky=W + E, ipadx=10, pady=15, padx=10)
        btnCancel = Button(self, text='Cancel', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6',
                           activeforeground='#FFFFFF', foreground='#FFFFFF')
        btnCancel.grid(row=3, column=2, sticky=W + E, ipadx=10, padx=10)



def StartWindow():
    root = Tk()
    root.title("Search")
    root.resizable(0, 0)
    app = Search(root)
    app.configure(background="white")
    root.mainloop()

"""Checks if given id is valid, and if it is - goes to the searchTut function and returns tutors id and name"""

def input_test(userinput):
    tutorInfo = []
    with open('fileLoc.txt') as txtFile:
           fileLocations = txtFile.readlines()
           fileLocations = [line.strip() for line in fileLocations]


    with open(fileLocations[0]) as tutorFile:

        with open(fileLocations[1]) as tuteeFile:
            tutorReader = csv.reader(tutorFile)
            tuteeReader = csv.reader(tuteeFile)
            found = False
            for row in tutorReader:

                if userinput == row[0]:
                    found = True
                    tutorInfo.append(row[0])
                    """Dealing with middle names"""

                    if row[3] == "":
                        name = row[1] + ' ' + row[2]
                    else:
                        name = row[1] + ' ' + row[3] + " " + row[2]
                    tutorInfo.append(name)
                    searchTut(userinput,tutorInfo,tuteeReader)

                    break
            if not found:
                messagebox.showerror("Input Error", "No such ID")
       


"""Gets all the students in a list fot the given tutor"""

def searchTut(tutid,info,tuteeFile):
    studentList = []
    for row in tuteeFile:
        childList =[]
        if tutid == row[4]:
                childList.append(row[0])

                """Dealing with middle names"""

                if row[3] == "":
                    name = row[1] + ' ' + row[2]
                else:
                    name = row[1] + ' ' + row[3] + " " + row[2]
                childList.append(name)
                studentList.append(childList)
    StartTree(studentList,info)




"""
Creates a new window, to output the table (should the code below be in a different file?)
"""



class Treelist(Frame):
    # GUI setup
    def __init__(self, master,sList,info):
        Frame.__init__(self, master)
        self.pack()
        self.list(sList,info)



    def list(self,sList,info):
        tree = ttk.Treeview(self)
        tree['show'] = 'headings'
        tree["columns"] = ("one", "two")
        tree.column("one", width=200)
        tree.column("two", width=200)
        tree.heading("one", text=info[0])
        tree.heading("two", text=info[1])

        for x in sList:
            tree.insert("", 0, text="Line 1", values=(x[0], x[1]))

        tree.pack()

def StartTree(sList,info):
    root = Tk()
    root.title("Tutees of " + info[1])
    root.minsize(200,200)

    app = Treelist(root,sList,info)
    app.configure(background="white")
    root.mainloop()





if __name__ == "__main__":
    import login



