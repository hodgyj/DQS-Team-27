import csv

class quota3():

	def data():

		# open csv files
		file1 = open('Tutors.csv')
		file2 = open('Tutees.csv')
		# read csv files
		tutor = csv.reader(file1)
		tutee = csv.reader(file2)
		# Store the csv files as lists
		tutorList = list(tutor)
		tuteeList = list(tutee)

		# list
		year1 = []
		year2 = []
		year3 = []
		year4 = []
		degreeGroup1 = []
		degreeGroup2 = []
		degreeGroup3= []
		degreeGroup4 = []

		#year
		for row in tutorList:
			for row2 in tuteeList:
				tutorID = row[0]
				tutorGroup = row2[4]
				if tutorID == "s1234" and tutorGroup == "s1234":
					year1.append(row2[6])
				elif tutorID == "s2345" and tutorGroup == "s2345":
					year2.append(row2[6])
				elif tutorID == "s3456" and tutorGroup == "s3456":
					year3.append(row2[6])
				elif tutorID == "s1352" and tutorGroup == "s1352":
					year4.append(row2[6])

		#degree
		for row in tutorList:
			for row2 in tuteeList:
				tutorID = row[0]
				tutorGroup = row2[4]
				if tutorID == "s1234" and tutorGroup == "s1234":
					degreeGroup1.append(row2[5])
				elif tutorID == "s2345" and tutorGroup == "s2345":
					degreeGroup2.append(row2[5])
				elif tutorID == "s3456" and tutorGroup == "s3456":
					degreeGroup3.append(row2[5])
				elif tutorID == "s1352" and tutorGroup == "s1352":
					degreeGroup4.append(row[5])

#######################################################

		# Jerry Springer

		JerryY1 = 0
		JerryY2 = 0
		JerryY3 = 0

		JerryD1 = 0
		JerryD2 = 0
		JerryD3 = 0
		JerryD4 = 0
		
		for i in year1:
			if i == '2016/17':
				JerryY1 += 1
			elif i == '2015/16':
				JerryY2 += 1
			else:
				JerryY3 += 1

		for i in degreeGroup1:
			if i == 'UFBSCMSB':
				JerryD1 += 1
			elif i == 'UFBSCMSA':
				JerryD2 += 1
			elif i == 'UFBSCSHA':
				JerryD3 += 1
			else:
				JerryD4 += 1

		# Boris Johnson

		BorisY1 = 0
		BorisY2 = 0
		BorisY3 = 0

		BorisD1 = 0
		BorisD2 = 0
		BorisD3 = 0
		BorisD4 = 0

		for i in year2:
			if i == '2016/17':
				BorisY1 += 1
			elif i == '2015/16':
				BorisY2 += 1
			else:
				BorisY3 += 1
		
		for i in degreeGroup2:
			if i == 'UFBSCMSB':
				BorisD1 += 1
			elif i == 'UFBSCMSA':
				BorisD2 += 1
			elif i == 'UFBSCSHA':
				BorisD3 += 1
			else:
				BorisD4 += 1

		# Volder Mort

		VolderY1 = 0
		VolderY2 = 0
		VolderY3 = 0

		VolderD1 = 0
		VolderD2 = 0
		VolderD3 = 0
		VolderD4 = 0

		for i in year3:
			if i == '2016/17':
				VolderY1 += 1
			elif i == '2015/16':
				VolderY2 += 1
			else:
				VolderY3 += 1
		
		for i in degreeGroup3:
			if i == 'UFBSCMSB':
				VolderD1 += 1
			elif i == 'UFBSCMSA':
				VolderD2 += 1
			elif i == 'UFBSCSHA':
				VolderD3 += 1
			else:
				VolderD4 += 1

		# Dude Bro Bruh

		DudeY1 = 0
		DudeY2 = 0
		DudeY3 = 0

		DudeD1 = 0
		DudeD2 = 0
		DudeD3 = 0
		DudeD4 = 0

		for i in year4:
			if i == '2016/17':
				DudeY1 += 1
			elif i == '2015/16':
				DudeY2 += 1
			else:
				DudeY3 += 1
		
		for i in degreeGroup4:
			if i == 'UFBSCMSB':
				DudeD1 += 1
			elif i == 'UFBSCMSA':
				DudeD2 += 1
			elif i == 'UFBSCSHA':
				DudeD3 += 1
			else:
				DudeD4 += 1

	print(data())