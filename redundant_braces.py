A = "(a+((b*((c+d)*e))+(f+g)))"
# A = "(((a+b+c+d)))"
# A = "((a + b + c + d))"
# A = "((a+b))"

op_list = ["+","-","*","/"]
stack = []
flag = 0
for i,char in enumerate(A):
	if char == "(" or char in op_list:
		stack.append(char)
	if char == ")":
		elem = stack.pop()
		print stack, elem
		if elem not in op_list:
			print "redundant brace!!"
			flag = 1
			break
		else:
			while stack[-1] != "(":
				stack.pop()
			stack.pop()
			print "removed:",stack

if flag==0:
	print "no redundant brace"