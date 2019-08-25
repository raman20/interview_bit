def add_one(A):
	A = "".join([str(i) for i in A])
       	A = int(A)
       	A = A+1
       	A = [int(i) for i in str(A)]
       	return A
