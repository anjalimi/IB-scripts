A = [ 4, 0, 2, 1, 3 ]


# for i,elem in enumerate(B):
# 	try: 
# 		A[i] = B[B[i]]

# 	except:
# 		print "Invalid Input"

# print A


# A=[A[j] for j in A]

# print (A)

# Works in O(n) space ---> add one element at a time in b, so that b is not passed by
# reference 

b=[]
for i in A:
    b.append(i)

i=0
while i<len(A):
    A[i]=b[b[i]]
    i=i+1
