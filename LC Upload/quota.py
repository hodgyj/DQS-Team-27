from tkinter import *
from tkinter import ttk
import csv

def getQuota():
    # Get names of the csv files
    with open('fileLoc.txt') as txtFile:
        fileLocations = txtFile.readlines()
        fileLocations = [line.strip() for line in fileLocations]
    # Opens and reads csv files
    with open(fileLocations[0]) as tutorFile:
        with open(fileLocations[1]) as tuteeFile:
            tutorReader = csv.reader(tutorFile)
            tuteeReader = csv.reader(tuteeFile)
            # Stores csv file contents as lists 
            tutorList = list(tutorReader)
            tuteeList = list(tuteeReader)

    tutorDict = {} 
    
    # Iterates through Tutor csv file
    for tutorRow in tutorList:
        quotaDict = {"degrees": {}, "years": {}, "num": 0} #
        # Iterates through Tutee csv file
        for tuteeRow in tuteeList:
            # If the student tutor group is equal to tutor ID
            if tuteeRow[4] == tutorRow[0]:
                # If student degree is equal to tutor degree group
                if tuteeRow[5] in quotaDict["degrees"]:  
                    quotaDict["degrees"][tuteeRow[5]] += 1
                else:
                    quotaDict["degrees"][tuteeRow[5]] = 1
                # If student year is equal to tutor degree group
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

        self.tblQuotas = ttk.Treeview(self, columns=2, height=8, padding=5, selectmode='extended', style='Treeview')
        self.tblQuotas.heading('#0', text='Tutor', anchor=CENTER)
        self.tblQuotas.heading('#1', text='Number of Tutees', anchor=CENTER)
        
        self.tblQuotas.grid(row=1, column=1, columnspan=2, pady=10)
        scrlBar = Scrollbar(self, command=self.tblQuotas.yview)
        self.tblQuotas.configure(yscrollcommand=scrlBar.set)
        scrlBar.grid(row=1, column=4, sticky=NW+SW)


        self.columnconfigure(0, minsize=20)
        self.columnconfigure(5, minsize=20)

    def getTutorName(self, tutorId):
        # Get names of the csv files
        with open('fileLoc.txt') as txtFile:
            fileLocations = txtFile.readlines()
            fileLocations = [line.strip() for line in fileLocations]

        with open(fileLocations[0]) as csvfile:
            reader = csv.reader(csvfile)
            for item in reader:
                if item[0] == tutorId:
                    tutorName = item[0] + " - " + item[1] + ", " + item[2] 
                    return tutorName

            return ""

    def displayQuota(self):
        # Gets the function that contains quota information
        quotaDict = getQuota()
        
        # Retrives tutor name, 
        for tutor, tutorDict in quotaDict.items():
            tutorName = self.getTutorName(tutor)
            rowId = self.tblQuotas.insert('', 'end', text=tutorName, values=(tutorDict['num']))
            degreeId = self.tblQuotas.insert(rowId, 'end', text='Degrees')
            yearId = self.tblQuotas.insert(rowId, 'end', text='Years')
            
            # Outputs the quota of tutees per degree group
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

if __name__ == "__main__":
    import login
