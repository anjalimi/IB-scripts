# A = ["4", "13", "5", "/", "+"]
A = ["2", "1", "+", "3", "*"]

# op_stack = []
# numerals =[]
operators = ["+","-","*","/"]

stack=[]
for i,elem in enumerate(A):
    if elem not in operators:
        stack.append(elem)
        print stack
    else:
        if len(stack)<2:
        	print 0
        	break
        else:
        	n1 = stack.pop()
        	n2 = stack.pop()
        	expression = n2+elem+n1
        	print expression
        	newNum = eval(expression)
        	stack.append(str(newNum))
        	print stack
print int(stack[0])


