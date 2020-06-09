# A = "/a//b/../../c/"

A = "/a/./b/../../c/"

# A = "/home/"

# A = "/../"
# A = "/home//foo/"

Alist = A.split("/")

if Alist[-1]=="":
	Alist.pop()

print Alist

simple = []
for char in Alist:

	if char == '':
		pass
	
	elif char == ".":
		pass 

	elif char == "..":
		if len(simple)!= 0:
			simple.pop()
	
	else:
		simple.append(char)

simple = "/".join(simple)

print "/"+simple