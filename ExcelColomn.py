theDict ={chr(y):(y-64) for y in range(65,91)}
print theDict

str1 = "BB"

len_str1 = len(str1)
mul_num = len_str1
col_num = 0

for i,elem in enumerate(str1):
	col_num = col_num + (26**(mul_num-1))*theDict[elem]
	mul_num-=1

print col_num



