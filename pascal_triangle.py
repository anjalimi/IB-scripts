numRows = 5

# Output = [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

Output=[[0 for j in range(i+1)]for i in range(numRows)]

for i in xrange(0,numRows):
	Output[i][0] = 1
	for j in range(1,i+1):
		if j == i:
			Output[i][j] = 1
		else:
			Output[i][j] = Output[i-1][j-1] + Output[i-1][j]

print Output