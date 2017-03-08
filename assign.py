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
		lblTitle = Label(self, text='Assign Student', font=('Segoe UI Light', 14,'bold'))
		lblTutor = Label(self, text='Please enter CSV filename for TUTORS: ', font=('Segoe UI', 8))
		lblTutee = Label(self, text='Please enter CSV filename for TUTEES: ', font=('Segoe UI', 8))
		lblTitle.grid(row=0, column=1, rowspan=1)
		lblTutor.grid(row=1, column=0, rowspan=1)
		lblTutee.grid(row=2, column=0, rowspan=1)

	def id(self):
		self.tutor = Entry(self)
		self.tutee = Entry(self)
		self.tutee.grid(row=2, column=1, columnspan=1, sticky=W)
		self.tutor.grid(row=1, column=1, columnspan=1, sticky=W)

	def buttons(self):
		butSubmit = Button(self, text='Ok', font=('Segoe UI', 8,'bold'))
		butClear = Button(self, text='Cancel', font=('Segoe UI', 8,'bold'))
		butClear['command']=self.clear
		butSubmit['command']=self.storeResponse
		butSubmit.grid(row=3, column=1, columnspan=1)
		butClear.grid(row=3, column=2, columnspan=1)

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