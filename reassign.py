from tkinter import * 
from tkinter import messagebox
import csv
import shutil

def reassignTutee(course, tutorsfile, tuteesfile):
    with open(tutorsfile) as csvfile:
        csvreader = csv.reader(csvfile)
        assigned = False
        # for each tutor if the course is the same as course student ias taking and they still have space left for more tutess, assign
        for row in csvreader:
            if (row[5] == course) and (numberOfStudents(row[0], tuteesfile) < int(row[4])):
                tutor = row[0]
                tutname = namer(row[2], row[3], row[1])
                assigned = True
                break

        # return to start of file for second iteration 
        csvfile.seek(0)

        # if student still hasn't been assigned, assign to tutor with enough space for more tutees
        if (assigned == False): 
            for row in csvreader:
                if (numberOfStudents(row[0], tuteesfile) < int(row[4])):
                    tutor = row[0]
                    tutname = namer(row[2], row[3], row[1])
                    assigned = True
                    break
        
        # if student still hasn't been assigned, leave tutor id and name variables blank
        if (assigned == False):      
            tutor = ""
            tutname = ""
    
    # close file and return tutor's id and name
    csvfile.close()
    return tutor, tutname

def filenames():
    file = open("fileLoc.txt", "r")

    tutorfile = str(file.readlines(1))
    tuteefile = str(file.readlines(2))
    
    for ch in ["'", "[", "]", "n", "\\"]:
        if ch in tutorfile:
            tutorfile = tutorfile.replace(ch, "")
        if ch in tuteefile:
            tuteefile = tuteefile.replace(ch, "")

    return tutorfile, tuteefile


def namer(firs, secon, last):
    # if student doesn't have a middle name set full name to just one space between first and sur name
    if (secon == ""):
        return (firs + " " + last)
    else:
        return (firs + " " + secon + " " + last)

def numberOfStudents(tutor, tuteesfile):
    # check how many tutees the tutor currently has assigned to them, by iterating through the tutee file
    number = 0
    with open(tuteesfile) as csvfile:
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
         butSubmit.grid(row=3, column=1, columnspan=2, sticky=W+E, pady=10, ipadx=2)

    def submitClicked(self):
        tutorsfile, tuteesfile = filenames()
        # collect user input and open tutee file, create a list out of it and iterate through list
        identity = self.entId.get()
        notutor = False
        with open(tuteesfile) as csvfile:
            csvreader = csv.reader(csvfile)
            lines = [line for line in csvreader]
            found = False
            for line in lines:
                if line[0] == identity:
                    # if id is found in file, attempt to reassign, if not possible output error message
                    found = True
                    tutor, tutname = reassignTutee(line[5], tutorsfile, tuteesfile)
                    if (tutor == ""):
                        messagebox.showerror("No Tutor Avaliable", "There is no tutor currently avaliable to take this student.")
                        notutor = True
                    else:
                        with open("temp.csv", "w", newline='') as tempfile:
                            # create new file to hold new list of tutees with updated tutor for student
                            csvwriter = csv.writer(tempfile)
                            name = line[2] + " " + line[3] + " " + line[1]
                            line[4] = tutor
                            csvwriter.writerows(lines)
                        tempfile.close()
                    break  
        csvfile.close()

        if (found == False):
            messagebox.showerror("Validation Error", "This is not a valid Student ID")
        elif (notutor == False):
            # override tutees file with temp file and delete temp file
            shutil.move("temp.csv", tuteesfile)
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