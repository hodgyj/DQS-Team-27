from tkinter import *
import csv
import shutil
import random

class Assign(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.idInput()
		self.id()
		self.buttons()

	def idInput(self):
		lblTitle = Label(self, text='Assign Student', font=('Segoe UI light', 24), background="white")
		lblTutor = Label(self, text='Please enter CSV \nfilename for TUTORS: ', font=('Segoe UI light', 16), background="white")
		lblTutee = Label(self, text='Please enter CSV \nfilename for TUTEES: ', font=('Segoe UI light', 16), background="white")
		lblTitle.grid(row=0, column=0, columnspan=3, sticky=W+E)
		lblTutor.grid(row=1, column=0, sticky=W, padx=10)
		lblTutee.grid(row=2, column=0, sticky=W, padx=10)

	def id(self):
		self.tutor = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
		self.tutee = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
		self.tutee.grid(row=2, column=1, sticky=E, padx=20)
		self.tutor.grid(row=1, column=1, sticky=E, padx=20)

	def buttons(self):
	 	butSubmit = Button(self, text='OK',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT, command=self.submitClicked)
	 	butSubmit.grid(row=4, column=1, columnspan=2, pady=10, ipadx=2)

	def submitClicked(self):
		try:
			csvFileName = self.tutee.get()
			tempFileName = "tempAssign.csv"

			text_file = open("fileLoc.txt", "w")
			text_file.write(self.tutor.get() + "\n" + self.tutee.get())
			text_file.close()

			if((self.tutor.index("end") == 0) or (self.tutee.index("end") == 0)):
				messagebox.showerror("Validation Error", "CSV file required in both fields.")
			else:
				file1 = open(self.tutor.get(), 'r')
				file2 = open(self.tutee.get(), 'r')

				tutor = csv.reader(file1)
				tutee = csv.reader(file2)

				tutorList = list(tutor)
				tuteeList = list(tutee)

				with open(tempFileName, 'w', newline='') as tempfile:
					wrt = csv.writer(tempfile)
					for row in tutorList:
						numberOfTutees = int(row[4])
						numAssigned = 0
						for row2 in tuteeList:
							degGroup = row[5]
							tutorID = row[0]
							degGroup2 = row2[5]
							if ((degGroup == degGroup2) and (numAssigned < numberOfTutees)):
								numAssigned += 1
								row2[4] = tutorID
							elif(numAssigned >= numberOfTutees):
								row2[4] = tutorList[random.randrange(0, 3)][0]
					
					for row in tuteeList:
						wrt.writerow(row)

				shutil.move(tempFileName, csvFileName)
				self.tutor.delete(0, END)
				self.tutee.delete(0, END)
				messagebox.showinfo("Successful", "All tutees assigned a tutor.")
		except FileNotFoundError:
			messagebox.showerror("Input error", "Oops! File not found.")

def StartWindow():
	root = Tk()
	root.title("Assign")
	root.resizable(0,0)
	app = Assign(root)
	app.configure(background="white")
	root.mainloop()

if __name__ == "__main__":
    import login 


