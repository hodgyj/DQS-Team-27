from tkinter import * 
from tkinter import messagebox
import csv

class Reassign(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createTitle()
		self.createIdEntry()
		self.Submit()

	def submitClicked(self):
		identity = self.entId.get()

		with open(filename) as csvfile:
			csvwriter = csv.writer(csvfile)
			csvreader = csv.reader(csvfile)
			found = False
			for row in csvreader:
				if row[0] == identity:
					row[4] = ""
					reassignTutee(identity, row[5], filename, tutfilename)
					found = True
			if not (found):
				mesagebox.askretrycancel("Validation Error", "This is not a valid Student ID")
	
	def reassignTutee(identity, course, filename, tutfilename):
		with open(tutfilename) as csvfile:
			csvreader = csv.reader(csvfile)
			for row in csvreader:
				if (row[5] == course) and (numberOfStudents(row[0], filename) < row[4]):
					tutor = row[0]
					with open(filename) as csvfile:
						csvwriter = csv.writer(csvfile)
						csvreader = csv.reader(csvfile)
						for row in csvreader:
							if row[0] == identity:
								row[4] = tutor

	def numberOfStudents(tutor, filename):
		number = 0
		with open(filename) as csvfile:
			csvreader = csv.reader(csvfile)
			for row in csvreader:
				if (row[4] == tutor):
					number += 1
		return number
	
	def openMain(self):
		root.destroy()
		import mainmenu
		mainmenu.StartWindow()

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

def StartWindow():
	root = Tk()
	root.title("Reassign Student")
	root.resizable(0,0)
	app = Reassign(root)
	app.configure(background="white")
	root.mainloop()

if __name__ == "__main__":
	import login