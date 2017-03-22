from tkinter import *
from tkinter import ttk
import csv

def getQuota():

    tutorList = []
    tuteeList = []

    with open('Tutors.csv') as tutorFile:
        with open('Tutees.csv') as tuteeFile:
            tutorReader = csv.reader(tutorFile)
            tuteeReader = csv.reader(tuteeFile)

            tutorList = list(tutorReader)
            tuteeList = list(tuteeReader)

    tutorDict = {}

    for tutorRow in tutorList:
        quotaDict = {"degrees": {}, "years": {}, "num": 0}
        for tuteeRow in tuteeList:
            if tuteeRow[4] == tutorRow[0]:
                if tuteeRow[5] in quotaDict["degrees"]:
                    quotaDict["degrees"][tuteeRow[5]] += 1
                else:
                    quotaDict["degrees"][tuteeRow[5]] = 1
                
                if tuteeRow[6] in quotaDict["years"]:
                    quotaDict["years"][tuteeRow[6]] += 1
                else:
                    quotaDict["years"][tuteeRow[6]] = 1
                
                quotaDict["num"] += 1
        tutorDict[tutorRow[0]] = quotaDict
    
    return tutorDict
    
class Quota(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createTitle()
        self.createTable()
        self.displayQuota()

    def createTitle(self):
        lblTitle = Label(self, text='Quotas', font=('Segoe UI Light', 32), background="white")
        lblTitle.grid(row=0, column=0, columnspan=4, sticky=W+E)

    def createTable(self):
        style = ttk.Style()
        style.configure('Treeview', font=('Segoe UI', 14))
        style.configure('Treeview', rowheight=30)

        self.tblQuotas = ttk.Treeview(self, columns=2, height=5, padding=5, selectmode='extended', style='Treeview')
        self.tblQuotas.heading('#0', text='Tutor ID', anchor=CENTER)
        self.tblQuotas.heading('#1', text='Number of Tutees', anchor=CENTER)
        
        self.tblQuotas.grid(row=1, column=1, columnspan=2, pady=10)
        scrlBar = Scrollbar(self, command=self.tblQuotas.yview)
        self.tblQuotas.configure(yscrollcommand=scrlBar.set)
        scrlBar.grid(row=1, column=4, sticky=NW+SW)


        self.columnconfigure(0, minsize=20)
        self.columnconfigure(5, minsize=20)


    def displayQuota(self):
        quotaDict = getQuota()

        for tutor, tutorDict in quotaDict.items():
            rowId = self.tblQuotas.insert('', 'end', text=tutor, values=(tutorDict['num']))
            degreeId = self.tblQuotas.insert(rowId, 'end', text='Degrees')
            yearId = self.tblQuotas.insert(rowId, 'end', text='Years')

            for degreeClass, numTutees in quotaDict[tutor]['degrees'].items():
                classRow = self.tblQuotas.insert(degreeId, 'end', iid=None, text=degreeClass, values=(numTutees))            
            
            for year, numTutees in quotaDict[tutor]['years'].items():
                yearRow = self.tblQuotas.insert(yearId, 'end', iid=None, text=year, values=(numTutees))



def StartWindow():
    root = Tk()
    root.title("Quotas")
    root.resizable(0,0)
    app = Quota(root)
    app.configure(background="white")
    root.mainloop()

StartWindow()