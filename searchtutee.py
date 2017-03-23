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
        lblTitle = Label(self, text='Tutee Search', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=5, padx=20)

    def createInput(self):
        lblHelp = Label(self, text='Please enter the tutee student number:', font=('Segoe UI Light', 16), background="white")
        lblHelp.grid(row=1, column=0, columnspan=3, sticky=W+E)

        txtSearch = Entry(self, font=('Segoe UI Light', 16), foreground="#2196F3", background="white")
        txtSearch.grid(row=2, column=1, sticky=W+E, ipadx=20)

        btnSearch = Button(self, text='Search', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF',
                           command = lambda : input_test(txtSearch.get()))
        btnSearch.grid(row=3, column=0, sticky=W+E, ipadx=10, pady=15, padx=10)

        btnCancel = Button(self, text='Cancel', font=('Segoe UI', 14), background='#2196F3', activebackground='#64B5F6', activeforeground='#FFFFFF', foreground='#FFFFFF')

        btnCancel.grid(row=3, column=2, sticky=W+E, ipadx=10, padx=10)



def input_test(userinput):
    # Get names of the csv files

    with open('fileLoc.txt') as txtFile:
           fileLocations = txtFile.readlines()
           fileLocations = [line.strip() for line in fileLocations]


    with open(fileLocations[0]) as tutorFile:

        with open(fileLocations[1]) as tuteeFile:
            tutorReader = csv.reader(tutorFile)
            tuteeReader = csv.reader(tuteeFile)
            studentInfo = []
            found = False
            for row in tuteeReader:

                if userinput == row[0]:
                        found = True
                        studentInfo.append(row[0])
                        """Dealing with middle names"""

                        if row[3] == "":
                            name = row[1] + ' ' + row[2]
                        else:
                            name = row[1] + ' ' + row[3] + " " + row[2]
                        studentInfo.append(name)
                        studentInfo.append(row[5])
                        studentInfo.append(row[6])
                        SearchTutee(studentInfo,row[4],tutorReader)

                        break

            if not found:
                    messagebox.showerror("Input Error", "No such ID")


def SearchTutee(info,tutor,tutorfile):


        for row in tutorfile:

            if tutor == row[0]:
                info.append(row[0])

                """Dealing with middle names"""

                if row[3] == "":
                    name = row[1] + ' ' + row[2]
                else:
                    name = row[1] + ' ' + row[3] + " " + row[2]
                info.append(name)

        StartTree(info)


def StartWindow():
    root = Tk()
    root.title("Search")
    root.resizable(0,0)
    app = Search(root)
    app.configure(background="white")
    root.mainloop()

"""
Creates a new window, to output the table (should the code below be in a different file?)
"""



class Treelist(Frame):
    # GUI setup
    def __init__(self, master,info):
        Frame.__init__(self, master)
        self.pack()
        self.list(info)



    def list(self,info):
        tree = ttk.Treeview(self)
        tree['show'] = 'headings'
        tree["columns"] = ("one", "two","three","four","five","six")
        tree.column("one", width=100)
        tree.column("two", width=200)
        tree.column("three", width=100)
        tree.column("four", width=100)
        tree.column("five", width=50)
        tree.column("six", width=200)
        tree.heading("one", text="student ID")
        tree.heading("two", text="Name")
        tree.heading("three", text = "Module")
        tree.heading("four", text = "Year")
        tree.heading("five", text = "TutorID")
        tree.heading("six", text = "Tutor Name")

        tree.insert("", 0, text="Line 1", values=(info[0], info[1],info[2],info[3],info[4],info[5]))

        tree.pack()

def StartTree(info):
    root = Tk()
    root.title(info[1])
    root.minsize(200,200)

    app = Treelist(root,info)
    app.configure(background="white")
    root.mainloop()





if __name__ == "__main__":
    import login








if __name__ == "__main__":
    import login


