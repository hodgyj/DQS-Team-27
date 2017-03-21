from tkinter import * 
from tkinter import messagebox
import csv
import shutil

def reassignTutee(course, filename, tutfilename):
    with open(tutfilename) as csvfile:
		assigned = False
		assigned2 = False
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if (row[5] == course) and (numberOfStudents(row[0], filename) < int(row[4])):
                tutor = row[0]
				assigned = True

		if (assigned == False):
    		for row in csvreader:
    			if (numberOfStudents(row[0], filename) < int(row[4])):
                	tutor = row[0]
					assigned2 = True
		
		if (assigned2 == False):
    		message.showerror("No Tutor Avaliable", "There is no tutor currently avaliable to take this student.")
		
    csvfile.close()
    return tutor

def numberOfStudents(tutor, filename):
    number = 0
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if (row[4] == tutor):
                number += 1
    csvfile.close()
    return number

class Reassign(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createTitle()
		self.createIdEntry()
		self.Submit()

	def createTitle(self):

		TitlePg = Label(self, text='Reassign Student', font=('Segoe UI light', 24), background="white")
		TitlePg.grid(row=0, column=0, columnspan=4, sticky=W+E)

	def createIdEntry(self):
		
		Label(self, text='Please enter ID of\nstudent to be reassigned:', 
			font=('Segoe UI light', 18), background="white").grid(row=1, column=0, columnspan=4, sticky=W+E, padx=15)
		self.entId=Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
		self.entId.grid(row=2, column=0, columnspan=4, sticky=W+E, padx=15)

	def Submit(self):

	 	butSubmit = Button(self, text='OK',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT, command=self.submitClicked)
	 	butSubmit.grid(row=3, column=1, columnspan=1, sticky=W, pady=10, ipadx=2)
	 	butCancel = Button(self, text='Cancel',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT, command=self.openMain)
	 	butCancel.grid(row=3, column=2, columnspan=1, sticky=E, pady=10, ipadx=2)

	def submitClicked(self):
    		identity = self.entId.get()
        with open("tutees.csv") as csvfile:
            with open("temp.csv", "w", newline='') as tempfile:
                csvreader = csv.reader(csvfile)
                csvwriter = csv.writer(tempfile)
                lines = [line for line in csvreader]
                found = False
                for line in lines:
                    if line[0] == identity:
                        tutor = reassignTutee(line[5], "tutees.csv", "tutors.csv")
                        line[4] = tutor
                        found = True
                        csvwriter.writerows(lines)
            tempfile.close()
        csvfile.close()
            
        if (found == False):
            messagebox.showerror("Validation Error", "This is not a valid Student ID")
        else:
            shutil.move("temp.csv", "tutees.csv")
            messagebox.showinfo("Reassigned Student", "Student Successfully Reassigned")
		
	def openMain(self):
		import mainmenu
		mainmenu.StartWindow()
	

def StartWindow():
	root = Tk()
	root.title("Reassign Student")
	root.resizable(0,0)
	app = Reassign(root)
	app.configure(background="white")
	root.mainloop()

if __name__ == "__main__":
	import login