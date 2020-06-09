dict1 = {"(":")","{":"}","[":"]"}
# print dict1.keys()

expression = ""

stack = []

if expression is "":
	print 0
for char in expression:
	if char in dict1.keys():
		stack.extend(char)
	else:
		check = stack.pop()
		if char == dict1[check]:
			continue
		else:
			print 0
			break

if stack == []:
	print 1