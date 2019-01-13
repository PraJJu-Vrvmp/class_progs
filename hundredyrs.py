class Name:
	def printing(name,age):
		print("Hey %s! You'll turn 100 years in %d"%(name,(2019+100-age)))

name = input("Enter name:")
age = eval(input("Enter age:"))
a=Name
a.printing(name,age)