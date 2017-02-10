#!/usr/bin/env python
class character(object):
	"""docstring for character"""
	def __init__(self, name, secondname, fakename, fakesecondname, age, job, records, medicalrecord, realrecord, gender):
		self.name = name
		self.secondname = secondname
		self.fakename = fakename
		self.fakesecondname = fakesecondname
		self.age = age if age < 99 else 99
		self.job = job
		self.records = records
		self.medicalrecord = medicalrecord
		self.realrecord = realrecord
		self.gender = gender

	def showData(self):
		print self.name
		print self.secondname
		print self.fakename
		print self.fakesecondname
		print self.age
		print self.job
		print self.records
		print self.medicalrecord
		print self.realrecord
		print self.gender
