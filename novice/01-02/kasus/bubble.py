def angka(x):

	for i in range (len(x)-1,0,-1):
		for j in range (i):
			if x[j]>x[j+1]:
				temp = x[j]
				x [j] = x[j+1]
				x[j+1] = temp
	
	print(x)

# no = [10,32,5,7,8,9,20,1,100]
# angka(no)
# print (no)