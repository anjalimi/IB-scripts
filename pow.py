

def pow(x, n):
	if n == 1: 
		return x
	elif n == 0:
		return 1
	elif n%2 ==0:
    	    return pow(x*x, n/2)
	else:
		return x*pow(x,n-1)
    


x = 71045970
n = 41535484
d = 64735492

print pow(x,n)


# num = x
# for i in range(1,n):
# 	num*=x

# print num%d