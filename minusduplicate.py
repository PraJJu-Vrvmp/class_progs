class Duplicate:
	def dup(lst):
		lst2 = []
		lst2.append(lst[0])
		lst1 = []
		lst1 = lst
		for i in range(len(lst2)):
			for j in range(1,(len(lst1))):
				if lst1[j] != lst[i]:
					lst2.append(lst1[j])
		print(lst2)
 
l = []
str = input("Enter values:")
l = str.split()
a = Duplicate
a.dup(l )