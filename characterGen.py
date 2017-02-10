#!/usr/bin/env python
import character, random

onejob = ["Head of Security","Research Director","Adminstrator"]

def genJobs():
	f = open("./resources/joblist.txt", "r")
	jobs = f.readlines()
	f.close
	f = open("./resources/finaljoblist.txt", "w")
	aux = jobs.pop()
	for i in range(random.randrange(6)):
			f.write(aux)
	"""if aux in onejob:
		f.write(aux)
	else:
		for i in range(random.randrange(6)):
			f.write(aux)"""
	f.close


	
def getRdName(n):
	f = open("./resources/first"+ n + ".txt", "r")
	newname = random.choice(f.readlines())
	f.close
	return newname

def getRdsecondName():
	f = open("./resources/last.txt", "r")
	newlast = random.choice(f.readlines())
	f.close
	return newlast

def getJob(antag):
	newjob = random.choice(listofjobs)
	return newjob

def mkcharacter():
	gender = "male" if random.randrange(2) == 1 else "female"
	name = getRdName(gender)
	secondname = getRdsecondName()
	if antag:
		fakename = getRdName(gender)
		fakesecondname = getRdsecondName()
	else:
		fakename = "none"
		fakesecondname = "none"

	age = random.randrange(50)

	job = getJob(antag)
	record = "ERROR_NOT_FILE_FOUND"
	medicalRecord = "ERROR_NOT_FILE_FOUND"
	realRecord = "ERROR_NOT_FILE_FOUND"

	newcharacter = character.character(name, secondname, fakename, fakesecondname, age, job, record, medicalRecord, realRecord, gender)

	return newcharacter
antag = random.randrange(2)
genJobs()
f = open("./resources/finaljoblist.txt", "r")
listofjobs = f.readlines()
f.close

primero = mkcharacter()
primero.showData()

