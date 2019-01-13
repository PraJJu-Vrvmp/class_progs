class Dict:
	def dic(n):
		lst1 = []
		lst2 = []
		for i in range(n):
			usn = input("Enter USN:")
			lst1.append(usn)
			name = input("Enter name:")
			lst2.append(name)
		d = dict(zip(lst1,lst2))
		print(d)

n = eval(input("Enter no. of inputs:"))
a = Dict
a.dic(n)