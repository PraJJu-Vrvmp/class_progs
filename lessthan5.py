class Less:
	def lessthan(lst):
		lst1 = []
		for i in range(len(lst)):
			if lst[i]<5:
				lst1.append(lst[i])
		print(lst1)

lst2 = []
lst2.extend(eval(input("Enter values:")))
a = Less
a.lessthan(lst2)