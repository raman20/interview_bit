# example :->

# If the vector has [1, 2, 3]

# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124


def add_one(A):
	A = "".join([str(i) for i in A])
       	A = int(A)
       	A = A+1
       	A = [int(i) for i in str(A)]
       	return A
