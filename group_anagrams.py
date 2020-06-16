# A = ["eat", "tea", "tan", "ate", "nat", "bat"]
# A = ["cat", "dog", "god", "tca"]

# A = [ "abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb" ]

A = [ "b", "b", "b", "a", "a", "b", "b", "b", "a", "b", "b", "a", "b", "b", "a", "a", "a", "a", "b", "b", "b", "a", "a", "b", "b", "a", "a", "a", "b", "b", "b", "a", "a", "b", "a", "a", "b", "b", "b", "b", "a", "a", "a", "a", "b", "b", "b", "a", "b", "a", "a", "a", "a", "b", "a", "b", "a", "b", "b", "a", "a", "a", "b", "b", "a", "a", "b", "b", "b", "b", "b", "b", "b", "a", "a", "b", "a", "a", "b", "a", "a", "a" ]

# A = ["eat","eat","ate","cat", "tac"]

def is_Anagram(A,B):
	if sorted(A) == sorted(B):
		return True
	return False

cache = {}
result = []
for i,elem in enumerate(A):
	if elem in cache:
		cache[elem].append(i+1)
	else:	
		cache.update({elem:[i+1]})

	for item in list(cache.keys()):
		if is_Anagram(elem,item) and elem!=item:
			if i+1 not in cache[item]:
				cache[item].append(i+1)							
			j = cache[item]
			cache.update({elem:j})

print cache

for item in cache:
	if cache[item] not in result:
		result.append(cache[item])

print sorted(result)