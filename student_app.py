from student import Student

#create at least 10 students

s1 = Student('Kevin', 'Chiteri')
s2 = Student('Allan', 'Mwesigwa', 'UG')
s3 = Student('Alvin', 'Mutisya')
s4 = Student('Rehema','Wachira')
s5 = Student('Elsis', 'Sitati')
s6 = Student('Stephen', 'Kanyi')
s7 = Student('Innocent', 'Kateba', 'TZ')
s8 = Student('Edison', 'Abahurire', 'UG')
s9 = Student('Blessing', 'Chimando', 'NG')
s10 = Student('Beth', 'Mwangi')
s11 = Student('Brian', 'Kimakoti')
s12 = Student('Didas', 'Mbalanya')
s13 = Student('Edward', 'Karanja')
s14 = Student('Winnie', 'Nyaguti')
s15 = Student('Samuel', 'Gaamuwa' 'UG')

s1.attend_class(id=s1.id,name=s1.fname,loc='Valhala',date='2016-08-20 07:30:41.094945')
s3.attend_class(id=s3.id,name=s3.fname,teacher= 'Nandaa')
s8.attend_class(id=s8.id,name=s8.fname,date='2016-08-20 07:30:41.094945')
s9.attend_class(id=s9.id,name=s9.fname,teacher='Nandaa',date='2016-08-20 07:30:41.094945')
s10.attend_class(id=s10.id,loc='Valhala',name=s10.fname,date='2016-08-20 07:30:41.094945')
s11.attend_class(id=s11.id,name=s11.fname,date='2016-08-20 07:30:41.094945')

roll_call8 = Student('','')

for item in roll_call8.students_attend_by_date(date='2016-08-20 07:30:41.094945'):
	print item
	


