def permute(nums):
    res = []
    if len(nums) == 1:
        res.append(nums)
        return res

    for elem in nums:
        rest = [e for e in nums if e!=elem]
        x = permute(rest)
        for item in x:
            item = item + [elem]
            if item not in res:
                res.append(item)

    return res


# L = ["foo", "bar"]
# L = [ "aaa", "aaa", "aaa", "aaa", "aaa" ]

L = [ "c", "b", "a", "c", "a", "a", "a", "b", "c" ]

uniq = []
for elem in L:
    same = [e for e in L if e==elem]
    same = "".join(same)
    if same not in uniq:
        uniq.append(same)
print uniq

p = permute(uniq)
print p

# S = "foobarthefoobarman

S = "bcabbcaabbccacacbabccacaababcbb"



res = []
for item in p:
    x = "".join(item)

    res+=[i for i in range(len(S)) if S.startswith(x, i)]

print res