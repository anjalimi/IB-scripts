def numTilePossibilities(tiles):
	"""
	:type tiles: str
	:rtype: int
	"""

	res = []
	for char in tiles:
		if char not in res:
			res.append(char)
		
	if len(tiles)==1:
		return res

	for i,elem in enumerate(tiles):
		x = numTilePossibilities(tiles[:i])
		y = numTilePossibilities(tiles[i+1:])		
		k = x+y
		print x,y,k
		for z in k:
			if elem+z not in res:
				res.append(elem+z)
	print res
	return res

# def numTilePossibilities(tiles):
#     def back2(path, s):
#         if len(path) != 0:
#             final_result.append(path)
#         used = []
#         for i in range(len(s)):
#             c = s[i]
#             if c in used:
#                 continue
#             used.append(c)
#             next_s = s[:i]
#             if i+1 < len(s):
#                 next_s += s[i+1:]
#             back2(path + [c], next_s)

#     final_result = []
#     back2([], tiles)
#     print final_result
#     return len(final_result)


S = "ABC"
print numTilePossibilities(S)