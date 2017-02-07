#!/usr/bin/python

import os, time, random

def startSession():

	dt = time.strftime("%d-%m-%y")

	tm = time.strftime("%H-%M")

	path = "./" + dt
	if not os.path.exists(path): os.makedirs(path)
	
	return (path, dt, tm)

def docMother(sN):


	n = open("docnames.txt", "r")

	

	namedoc = "MetaDoc"

	path =  sN[0] + "/" + namedoc +".txt" 
	f = open( path ,"w")

	f.write("This is a test " + path + "This is the time: "+ sN[1] + sN[2])

	if n.read(1) == "D":
		print "REEEEEEEEE"
	else:
		print "AAAAAAAA"
	

	f.close
	n.close

def getPutWord(words, newWords, document):
	print document
	l = open( document , "r+" )
	d = l.read()
	print d.count("i")
	print type(d)
	l.write(d)
	l.close
sessionNames = startSession()

def pjMaker():
	print "Generating a new one..."
	print "getting gender..."
	dirNames = "./"
	valor = random.randint(0,1)
	if valor == 1:
		gender = "male"
	else:
		gender = "female"
	l = open( dirNames + "first" + gender + ".txt" , "r" )
	auxl = l.read()
	name = random.choice(auxl)
	print name
	l.close
	l = open( dirNames + "last" + ".txt" , "r" )
	auxl = l.read()
	name = name + random.choice(auxl)
	print name
	l.close
	
	return name

docMother(sessionNames)

pj = pjMaker()
print pj




