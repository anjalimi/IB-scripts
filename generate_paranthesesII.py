def generateParenthesis(N):
	# res = []
	# if A == 0:
	# 	return res
	# if A == 1:
	# 	s = "()"
	# 	res.append(s)
	# 	return res

	# x = generateParenthesis(A-1)
	
	# for items in x:
	# 	s1 = "("+items+")"
	# 	if s1 not in res:
	# 		res.append(s1)
	# 	s2 = "()"+items
	# 	if s2 not in res:
	# 		res.append(s2)
	# 	s3 = items+"()"
	# 	if s3 not in res:
	# 		res.append(s3)
	# print sorted(res)
	# return res
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return ans



A = 4
print generateParenthesis(A)

# N = 3
# "((()))", "(()())", "(())()", "()(())", "()()()"
# N = 2
# (()) ()() 
# N = 1
# ()

# (((()))) ((()())) ((())()) ((()))() (()(())) (()()()) (()())() (())(()) (())()() ()((())) ()(()()) ()(())() ()()(()) ()()()()
# (((()))) ((()())) ((())()) ((()))() (()(())) (()()()) (()())() (())()() ()((())) ()(()()) ()(())() ()(())() ()()(()) ()()()()