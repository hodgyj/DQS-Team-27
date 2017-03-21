import csv
import shutil

csvFileName = "tutees.csv"
tempFileName = "tempAssign.csv"

file1 = open('tutors.csv', 'r')
file2 = open('tutees.csv', 'r')

tutor = csv.reader(file1)
next(tutor)
tutee = csv.reader(file2)


with open(tempFileName, 'w', newline='') as tempfile:
	wrt = csv.writer(tempfile)
	for row in tutor:
		for row2 in tutee:
			degGroup = row[5]
			tutorID = row[0]
			degGroup2 = row2[5]
			if degGroup == degGroup2:
				row2[4] = tutorID
				wrt.writerow(row2)
			else:
				wrt.writerow(row2)

shutil.move(tempFileName, csvFileName)
