from tkinter import *
import csv

class Quota(Frame):

	def findTutor():

		Tutors = csv.reader(open("Tutors.csv"))
		Tutees = csv.reader(open("Tutees.csv"))

		for row in Tutors:
			for row in Tutees:
				if row[0] == row[4]

	def searchYear():
		
		Year1 = 0
		Year2 = 0
		Year3 = 0	

		rdr = csv.reader(open("Tutees.csv"))
		for row in rdr:
			if row[6] == "2016/17":
				Year1 += 1
			elif row[6] == "2015/16":
				Year2 += 1
			elif row[6] == "2014/15":
				Year3 += 1
		return Year1
		return Year2
		return Year3

	def searchDegree():

		Degree1 = 0 
		Degree2 = 0
		Degree3 = 0
		Degree4 = 0

		rdr = csv.reader(open("Tutees.csv"))	
		for row in rdr:
			if row[5] == "UFBSCMSA":
				Degree1 += 1
			elif row[5] == "UFBSCMSB":
				Degree2 += 1
			elif row[5] == "UFBSASEA":
				Degree3 += 1
			elif row[5] == "UFBSCSHA":
				Degree4 += 1			
		return Degree1
		return Degree2
		return Degree3
		return Degree4