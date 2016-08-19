from datetime import datetime
class Student(object): #object allows for inheritance
	map_ = {
	'KE':'Kenya',
	'UG':'Uganda',
	'TZ':'Tanzania',
	'NG':'Nigeria'
	}
	
	id_holder = 0
	attends=[]

	def __init__(self, fname, lname, country='KE'): #a function within a class is a method
		Student.id_holder +=1
		self.id =Student.id_holder
		self.fname = fname
		self.lname = lname
		self.country = Student.map_[country]

	def attend_class(self,**kwargs):
		self.loc = kwargs.setdefault('loc','Hogwarts')
		self.date=kwargs.setdefault('date',datetime.today().date())
		self.teacher=kwargs.setdefault('teacher','Alex')

		#add those attend class to the list
		Student.attends.append(kwargs)

	def students_attend_by_date(self,date):
		students = []
		for student in Student.attends:
			if student['date'] is date:
				students.append(student)
		return students


