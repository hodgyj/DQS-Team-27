from tkinter import * 

class Reassign(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()
		self.createTitle()
		self.createIdEntry()
		self.Submit()

	def createTitle(self):

		TitlePg = Label(self, text='Reassign Student', font=('Segoe UI light', 24))
		TitlePg.grid(row=0, column=0, columnspan=6, sticky=W+E)


	def createIdEntry(self):
		
		Label(self, text='Please enter ID of\nstudent to be reassigned:', 
			font=('Segoe UI light', 20)).grid(row=2)
		self.entId=Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
		self.entId.grid(row=2, column=2, columnspan=4, sticky=E)

	def Submit(self):

	 	butSubmit = Button(self, text='OK',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT)
	 	butSubmit.grid(row=4, column=0, columnspan=2, pady=10, ipadx=2)
	 	butCancel = Button(self, text='Cancel',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT)
	 	butCancel.grid(row=4, column=2, columnspan=2, pady=10, ipadx=2)


root = Tk()
root.title("Reassign Student")
root.resizable(0,0)
app = Reassign(root)
root.mainloop()