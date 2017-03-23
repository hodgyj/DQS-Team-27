from tkinter import * 
from tkinter import messagebox
import csv
import shutil

def reassignTutee(course, filename, tutfilename):
    with open(tutfilename) as csvfile:
        csvreader = csv.reader(csvfile)
        assigned = False

        for row in csvreader:
            if (row[5] == course) and (numberOfStudents(row[0], filename) < int(row[4])):
                tutor = row[0]
                tutname = namer(row[2], row[3], row[1])
                assigned = True
                break

        csvfile.seek(0)

        if (assigned == False): 
            for row in csvreader:
                if (numberOfStudents(row[0], filename) < int(row[4])):
                    tutor = row[0]
                    tutname = namer(row[2], row[3], row[1])
                    assigned = True
                    break
            
        if (assigned == False):      
            tutor = ""
            tutname = ""
        
    csvfile.close()
    return tutor, tutname

def namer(firs, secon, last):
    if (secon == ""):
        return (firs + " " + last)
    else:
        return (firs + " " + secon + " " + last)

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
         butSubmit.grid(row=3, column=2, columnspan=1, sticky=W+E, pady=10, ipadx=2)

    def submitClicked(self):
        identity = self.entId.get()
        notutor = False
        with open("tutees.csv") as csvfile:
            with open("temp.csv", "w", newline='') as tempfile:
                csvreader = csv.reader(csvfile)
                csvwriter = csv.writer(tempfile)
                lines = [line for line in csvreader]
                found = False
                for line in lines:
                    if line[0] == identity:
                        found = True
                        tutor, tutname = reassignTutee(line[5], "tutees.csv", "tutors.csv")
                        if (tutor == ""):
                            messagebox.showerror("No Tutor Avaliable", "There is no tutor currently avaliable to take this student.")
                            notutor = True
                        else:
                            name = line[2] + " " + line[3] + " " + line[1]
                            line[4] = tutor
                            csvwriter.writerows(lines)
            tempfile.close()
        csvfile.close()
            
        if (found == False):
            messagebox.showerror("Validation Error", "This is not a valid Student ID")
        elif (notutor == False):
            shutil.move("temp.csv", "tutees.csv")
            messagebox.showinfo("Reassigned Student Successfully", "Student:   " + name + ", " + identity + " \nReassigned to \nTutor:       " + tutname + ", " + tutor)
            self.entId.delete(0, END)

def StartWindow():
    root = Tk()
    root.title("Reassign Student")
    root.resizable(0,0)
    app = Reassign(root)
    app.configure(background="white")
    root.mainloop()

if __name__ == "__main__":
    import login