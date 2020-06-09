A = "XIV"
roman_dict  = {
	"I":1,
	"V":5,
	"X":10,
	"L":50,
	"C":100,
	"D":500,
	"M":1000
}

val = 0
for i,char in enumerate(A):
	curr_val = roman_dict[char]
	# print curr_val

	if i != 0:
		if roman_dict[A[i-1]] < roman_dict[char]:
			# print "before sub", val
			val = val - (2*roman_dict[A[i-1]]) + curr_val
			# print "after sub",val
			continue

	val += curr_val

print val