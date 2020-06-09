# A = "AACEECAAAA"
# A = "ABBC"
A = "eylfpbnpljvrvipyamyehwqnq"
# ind = 0
# # for i,char in enumerate(A):
# i = 0
# substring = ""
# maxstring = ""
# while i != len(A):
# 	# print A[i]
# 	substring += A[i]
# 	print "Sub: ",substring
# 	if substring[::-1] in A[i+1:]:
# 		print "rotated sub: ",substring[::-1]
# 		maxstring = max([substring,maxstring],key=len)
# 		print "Max: ",maxstring
# 	else:
# 		substring = ""
# 		ind = i-1
# 		break

# 	i += 1

# print maxstring,ind

# if maxstring is A[0]:
# 	print len(A) - 1
# else:
# 	print len(A) - len(maxstring)

A = list(A)
print A
k = len(A)
count = 0
while(k>0):
    if(A==A[::-1]):
        print count
        break
    else:
        count+=1
        k-=1
        A.pop()
        print A

