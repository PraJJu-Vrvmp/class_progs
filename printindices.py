class Indices:
	def ind(lst,src):
		lst1 = []
		for i in range(len(lst)):
			if src == lst[i]:
				lst1.append(i)
		print(lst1)

lst = []
inp = input("Enter values:")
lst = inp.split()
src = input("Enter search element:")
a = Indices
a.ind(lst,src)