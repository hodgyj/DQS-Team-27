from tkinter import *
class Assign(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.idInput()
		self.id()
		self.buttons()
		self.clear()

	def idInput(self):
		lblTitle = Label(self, text='Assign Student', font=('Segoe UI light', 24))
		lblTutor = Label(self, text='Please enter CSV \nfilename for TUTORS: ', font=('Segoe UI light', 18))
		lblTutee = Label(self, text='Please enter CSV \nfilename for TUTEES: ', font=('Segoe UI light', 18))
		lblTitle.grid(row=0, column=0, columnspan=3, sticky=W+E)
		lblTutor.grid(row=1, column=0, sticky=W)
		lblTutee.grid(row=2, column=0, sticky=W)

	def id(self):
		self.tutor = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
		self.tutee = Entry(self, font=('Segoe UI', 18), fg='#2196F3', bg='white')
		self.tutee.grid(row=2, column=1, sticky=E, padx=20)
		self.tutor.grid(row=1, column=1, sticky=E, padx=20)

	def buttons(self):
	 	butSubmit = Button(self, text='OK',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT)
	 	butSubmit.grid(row=4, column=0, columnspan=1, pady=10, ipadx=2)
	 	butCancel = Button(self, text='Cancel',font=('Segoe UI light', 14), bg='#2196F3', activebackground='#64B5F6', fg='white', activeforeground='white', relief=FLAT)
	 	butCancel.grid(row=4, column=1, columnspan=1, pady=10, ipadx=2)

	def clear(self):
		self.tutor.delete(0, END)
		self.tutee.delete(0, END)

	def storeResponse(self):
		strMsgReassign=""
		if (self.tutor.index("end") == 0) or (self.tutee.index("end") == 0):
			strMsgReassign = "Both fields must be completed."

root = Tk()
root.title("Assign")
app = Assign(root)
root.mainloop() 